import logging
import pandas as pd
import numpy as np
from lightgbm import LGBMClassifier
from sklearn.base import BaseEstimator
from sklearn.exceptions import NotFittedError
from sklearn.utils.validation import check_is_fitted
DEFAULT_MODEL = LGBMClassifier
LGBM_PARAMS = ['learning_rate', 'num_leaves', 'min_data_in_leaf']


class AdHocBoostBase:
    """
    AdHocBoost classifier, a model specialized for binary classification in a severely imbalanced-class scenario.

    The AdHocBoost model works by creating n sequential LGBM classifiers. The first n-1 classifiers can most aptly be
    thought of as dataset filtering models, i.e. each one does a good job at classifying rows as "definitely not the
    positive class" versus "maybe the positive class". The nth model only works on this filtered "maybe positive" data.
    """

    def __init__(self):
        """
        Init function.
        """
        pass

    def fit(self, train_X, train_y) -> None:
        """
        Fit the model.
        :param train_X: The train feature-array, of shape (n-samples, n-features)
        :type train_X: numpy nd array
        :param train_y: The train label-array, of shape (n-samples,)
        :type train_y: numpy 1d array
        """

        # Create a dataframe for tracking the predicted probability of each model.
        logging.info(f"Fitting entire model pipeline.")
        stage_prediction_df = pd.DataFrame({
            f"stage{stage_number}": np.zeros(train_X.shape[0])
            for stage_number in range(self.number_stages)})

        # For each model, fit it, then do a prediction on the train data and log it to `stage_prediction_df`
        for stage_number in range(self.number_stages):

            # Get this stage's training data as whatever's left from the prior stage's model filtering.
            if stage_number == 0:
                stage_mask = np.ones(train_X.shape[0], dtype=bool)
            else:
                proba_threshold = self.get_stage_proba_threshold(stage_number - 1)
                logging.info(f"Getting all data for stage{stage_number}--filter predicted probabilities from "
                             f"stage{stage_number - 1} by threshold {proba_threshold}")
                stage_mask = (stage_prediction_df[f"stage{stage_number - 1}"] >
                              proba_threshold).to_numpy()

            # If the probability threshold has been set too high, then there's no data to train the second model.
            # Catch this case and exit the model training early.
            try:
                assert stage_mask.sum() > 0
            except AssertionError as e:
                logging.error(f"There is no data to train for stage {stage_number}, because it has all been filtered "
                              f"out. Consider lowering the probability thresholds of prior stages. Exiting fitting.")
                raise e

            # Fit the stage model.
            stage_sample_weight = self.get_sample_weight_column(
                train_y[stage_mask],
                positive_sample_weight=self.get_stage_sample_weight(stage_number))
            self.fit_stage_model(
                train_X[stage_mask],
                train_y[stage_mask],
                stage_sample_weight,
                stage_number=stage_number)

            # Do a prediction on the train data and log it to `stage_prediction_df`. The prediction only needs to be run
            # on the stage_mask rows, hence the filter.
            stage_prediction = self.stage_predict_proba(train_X[stage_mask], stage_number)
            stage_prediction_df.loc[stage_mask, f"stage{stage_number}"] = stage_prediction

        # log
        logging.info(f"Fitting completed.")

    def fit_stage_model(self, stage_train_X, stage_train_y, stage_sample_weight, stage_number=0) -> None:
        """
        Fits the stage_number'th model.
        :param stage_train_X: The train feature-array, of shape (n-samples, n-features)
        :type stage_train_X: numpy nd array
        :param stage_train_y: The train label-array, of shape (n-samples,)
        :type stage_train_y: numpy 1d array
        :param stage_sample_weight: A column of sample weights, of shape (n-samples,)
        :type stage_sample_weight: numpy 1d array
        :param stage_number: The stage number model that is being fit.
        :type stage_number: int
        :return:
        """
        logging.info(f"Fitting stage {stage_number} model with {stage_train_X.shape[0]} data points, "
                     f"weighting the positive class by {stage_sample_weight.max()}...")
        model = self.get_stage_model(stage_number)
        model.fit(
            stage_train_X,
            stage_train_y,
            sample_weight=stage_sample_weight)

    def get_sample_weight_column(self, y, positive_sample_weight=1) -> np.array:
        """
        Gets sample-weight column for use in fitting a model. The negative class is weighted as `1`, and the positive
        class is weighted as `positive_sample_multiplier * sqrt(|Positives| / |Negatives|)`.
        :param positive_sample_weight:
        :param y: Array of labels.
        :type y: np.array
        :return:
        """
        sample_weight_column = np.ones(y.shape[0])
        sample_weight_column[y == 1] = positive_sample_weight
        return sample_weight_column

    def stage_predict_proba(self, data, stage_number) -> np.array:
        logging.info(f"Predicting proba on stage {stage_number} ({data.shape[0]} data points)...")
        return self.get_stage_model(stage_number).predict_proba(data)[:, 1]

    def stage_predict(self, data, stage_number) -> np.array:
        logging.info(f"Predicting label on stage {stage_number} ({data.shape[0]} data points)...")
        return self.get_stage_model(stage_number).predict(data)

    def predict_proba(self, data, predict_labels=False) -> np.array:
        """
        Predict probabilities.
        :param data: A feature-array, of shape (n-samples, n-features)
        :type data: np.array
        :param predict: Boolean that indicates whether to predict labels or just predict probabilities.
        :type predict: bool
        :return: pd.Series of predictions (either labels or probabilities)
        """

        # Before predicting, check if the model has been fitted
        self.is_fitted()

        # Create a dataframe for tracking the prediction from each stage.
        logging.info(f"Predicting {'label' if predict_labels else 'proba'} from entire model pipeline:")
        stage_prediction_df = pd.DataFrame({
            f"stage{stage_number}": np.zeros(data.shape[0])
            for stage_number in range(self.number_stages - 1)
        })
        stage_prediction_df[f"stage{self.number_stages - 1}"] = \
            np.zeros(data.shape[0], dtype=bool if predict_labels else float)

        # For each model, do a prediction on the data and log it to `stage_prediction_df`
        for stage_number in range(self.number_stages):

            # Get the stage's mask.
            if stage_number == 0:
                stage_mask = np.ones(data.shape[0], dtype=bool)
            else:
                proba_threshold = self.get_stage_proba_threshold(stage_number - 1)
                logging.info(
                    f"Getting all data for stage{stage_number}--filter predicted probabilities from "
                    f"stage{stage_number - 1} by threshold {proba_threshold}")
                stage_mask = (stage_prediction_df[f"stage{stage_number - 1}"] >
                              proba_threshold).to_numpy()

            # Do a prediction on the data and log it to `stage_prediction_df`. The prediction only needs to be run
            # on the stage_mask rows, hence the filter.
            if (stage_number == self.number_stages - 1) and (predict_labels == True):
                stage_prediction = self.stage_predict(data[stage_mask], stage_number)
            else:
                stage_prediction = self.stage_predict_proba(data[stage_mask], stage_number)
            stage_prediction_df.loc[stage_mask, f"stage{stage_number}"] = stage_prediction

        # Return the last stage's predictions.
        # To conform with sklearn api of returning array of shape (n_rows, n_classes), a column of zeros is appended to
        # the left of the predicted probabilities.
        predicted_probas = stage_prediction_df[f"stage{self.number_stages - 1}"].to_numpy().reshape((-1, 1))
        return np.hstack([np.zeros((predicted_probas.shape[0], 1)), predicted_probas])

    def predict(self, data) -> np.array:
        """
        Predict labels.
        :param data: A feature-array, of shape (n-samples, n-features)
        :type data: np.array
        :return: pd.Series of predicted labels
        """

        # Before predicting, check if the model has been fitted
        self.is_fitted()

        # return prediction
        return self.predict_proba(data, predict_labels=True)

    def is_fitted(self) -> None:
        """
        Helper function to check if the model has been completely trained or not. Returns None or raises an error.
        :return: None
        """
        try:
            for i, model in enumerate(self.stage_models):
                print(i, model)
                print(check_is_fitted(model))
        except NotFittedError as e:
            logging.error(f"Model is not completely fitted; cannot execute prediction.")
            raise e

    def get_stage_model(self, stage_number: int):
        """
        Get helper function; gets and returns the stage_number'th model.
        :param stage_number: Model to retrieve
        :type stage_number: int
        :return: A model of type self.stage_model_cls.
        """
        return self.stage_models[stage_number]

    def get_stage_sample_weight(self, stage_number: int) -> float:
        """
        Getter helper function; gets and returns the stage_number'th sample_weight_multiplier.
        :param stage_number: Sample weight to retrieve
        :type stage_number: int
        :return: float
        """
        return self.stage_positive_sample_weights[stage_number]

    def get_stage_proba_threshold(self, stage_number: int) -> float:
        """
        Getter helper function; gets and returns the stage_number'th probability threshold.
        :param stage_number: Model to retrieve
        :type stage_number: int
        :return: A model of type self.stage_model_cls.
        """
        return self.stage_proba_thresholds[stage_number]


class AdHocBoostLGBM(AdHocBoostBase, BaseEstimator):

    def __init__(self, number_stages: int = 2, positive_sample_weight_0: float = 0.17, learning_rate_0: float = 0.1,
                 num_leaves_0: int = 30, min_data_in_leaf_0: int = 17, proba_threshold_0: float = 0.2,
                 positive_sample_weight_1: float = 0.10, learning_rate_1: float = 0.05, num_leaves_1: int = 33,
                 min_data_in_leaf_1: int = 19):

        super().__init__()
        self.number_stages = number_stages
        self.positive_sample_weight_0 = positive_sample_weight_0
        self.learning_rate_0 = learning_rate_0
        self.num_leaves_0 = num_leaves_0
        self.min_data_in_leaf_0 = min_data_in_leaf_0
        self.proba_threshold_0 = proba_threshold_0
        self.positive_sample_weight_1 = positive_sample_weight_1
        self.learning_rate_1 = learning_rate_1
        self.num_leaves_1 = num_leaves_1
        self.min_data_in_leaf_1 = min_data_in_leaf_1

        # initialize emptpy variables
        self.stage_proba_thresholds = None
        self.stage_positive_sample_weights = None
        self.stage_model_hyper_param_sets = None
        self.stage_models = None

    def _init_model(self):

        # process the params from __init__
        self.stage_proba_thresholds = [getattr(self, f'proba_threshold_{i}')
                                       for i in range(self.number_stages - 1)]
        self.stage_positive_sample_weights = [getattr(self, f'positive_sample_weight_{i}')
                                              for i in range(self.number_stages)]
        self.stage_model_hyper_param_sets = [{param: getattr(self, f'{param}_{i}') for param in LGBM_PARAMS}
                                             for i in range(self.number_stages)]

        # create the models
        self.stage_models = [LGBMClassifier(**hyper_param_set, objective="binary") for hyper_param_set in
                             self.stage_model_hyper_param_sets]

    def fit(self, train_X, train_y) -> None:

        # initialize the model
        logging.info("Initializing the stage models.")
        self._init_model()

        # super fit
        super().fit(train_X, train_y)