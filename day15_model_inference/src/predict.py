import joblib
import pandas as pd
import os

# Get absolute path of this file (predict.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build absolute paths
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "best_model.pkl")
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "sample_input.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "..", "data", "predictions_output.csv")

# Load model
model = joblib.load(MODEL_PATH)

# Load data
data = pd.read_csv(DATA_PATH)

# Predict
predictions = model.predict(data)

# Save output
data["Predicted_Item_Outlet_Sales"] = predictions
data.to_csv(OUTPUT_PATH, index=False)

print("Day 15 completed successfully")
