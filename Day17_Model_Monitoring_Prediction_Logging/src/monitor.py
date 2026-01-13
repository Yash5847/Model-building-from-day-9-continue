import pickle
import pandas as pd
from datetime import datetime
import os

# Paths
MODEL_PATH = "models/best_model.pkl"
LOG_PATH = "logs/prediction_logs.csv"

# Load trained model
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

def log_prediction(input_df, prediction):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = {
        "timestamp": timestamp,
        "input_data": input_df.to_json(orient="records"),
        "prediction": prediction.tolist()
    }

    log_df = pd.DataFrame([log_entry])

    # Append logs
    if os.path.exists(LOG_PATH):
        log_df.to_csv(LOG_PATH, mode="a", header=False, index=False)
    else:
        log_df.to_csv(LOG_PATH, index=False)

def predict_and_log(input_df):
    prediction = model.predict(input_df)
    log_prediction(input_df, prediction)
    return prediction
