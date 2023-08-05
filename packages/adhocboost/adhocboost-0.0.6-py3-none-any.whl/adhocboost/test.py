from lightgbm import LGBMClassifier
import pandas as pd
from AdHocBoostBase import AdHocBoostLGBM, AdHocBoostBase
import numpy as np
from sklearn.metrics import precision_recall_curve, average_precision_score
import matplotlib.pyplot as plt
import logging
import os

# Create constants.
ENTITY = 'FP_PK'
TARGET = 'is_address_cancelled'
PREDICTORS = [
    "address_line1_is_null",
    "address_line2_is_null",
    "address_line3_is_null",
    "address_line4_is_null",
    "address_other_is_null",
    "address_building_is_null",
    "address_city_is_null",
    "address_delivery_instructions_is_null",
    "address_count_past_address_cancellations",
    "customer_count_past_address_cancellations",
    "address_order_rank",
    "address_median_dropoff_error",
    "address_median_at_customer_time",
    "address_latitude",
    "address_longitude"
]

# Load the data.
entity = "FP_MM"
train_data_path = f"/Users/b.feifke/code/pd-location-ml-pipeline/scripts/data/" \
                  f"{entity}_orders_df_2021-09-01_2021-10-20.parquet"
test_data_path = f"/Users/b.feifke/code/pd-location-ml-pipeline/scripts/data/" \
                 f"{entity}_orders_df_2021-10-21_2021-10-31.parquet"
train_data = pd.read_parquet(train_data_path)
test_data = pd.read_parquet(test_data_path)
for data in train_data, test_data:
    for field in ['address_latitude', 'address_longitude']:
        data[field] = data[field].astype(float)
positive_negative_sample_ratio = (train_data[TARGET] == False).sum() / (train_data[TARGET] == True).sum()

# create adhocboost model
adhocboost_model = AdHocBoostLGBM(positive_sample_weight_0=1.975 * np.sqrt(positive_negative_sample_ratio),
                                  positive_sample_weight_1=1.788 * np.sqrt(positive_negative_sample_ratio))
adhocboost_model.fit(train_data[PREDICTORS], train_data[TARGET])
print(adhocboost_model.get_params())

# create lgbm model
lgbm_model = LGBMClassifier(learning_rate=0.035,
                            num_leaves=28,
                            min_data_in_leaf=22,
                            objective="binary")
lgbm_model.fit(
    train_data[PREDICTORS].to_numpy(),
    train_data[TARGET].to_numpy().flatten(),
    sample_weight=1.03 * np.sqrt(positive_negative_sample_ratio))

# eval
for model, name in zip([lgbm_model, adhocboost_model], ['lgbm_model', 'adhocboost_model']):
    y_pred = model.predict_proba(test_data[PREDICTORS])[:, 1]
    precision_array, recall_array, thresholds_array = precision_recall_curve(test_data[TARGET],
                                                                             y_pred)
    average_precision = average_precision_score(test_data[TARGET],
                                                y_pred)
    plt.plot(recall_array, precision_array, label=f"{name} (AP={average_precision:.3f})")
plt.xlabel('recall')
plt.ylabel('precision')
plt.legend()
plt.title(f'Precision Recall Curves, {entity}')
plt.show()