import pandas as pd
import joblib
import os
from datetime import datetime

model = joblib.load("../models/model.pkl")

os.makedirs("../logs", exist_ok=True)
LOG_FILE = "../logs/predictions_log.csv"

def predict_and_log(input_df):
    prediction = model.predict(input_df)

    log_df = input_df.copy()
    log_df["prediction"] = prediction
    log_df["timestamp"] = datetime.now()

    if os.path.exists(LOG_FILE):
        log_df.to_csv(LOG_FILE, mode="a", header=False, index=False)
    else:
        log_df.to_csv(LOG_FILE, index=False)

    return prediction
