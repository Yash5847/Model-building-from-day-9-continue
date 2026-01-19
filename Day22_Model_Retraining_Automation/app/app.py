from flask import Flask, request, jsonify
import pandas as pd
import pickle, logging, os

app = Flask(__name__)

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

MODEL_PATH = r"C:\Users\Yash\OneDrive\Desktop\ML_Project\models\best_model.pkl"

model = None
try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    logging.info("Model loaded successfully")
except Exception as e:
    logging.error(f"Model loading failed: {e}")
    model = None


@app.route("/")
def home():
    return "API is running"


@app.route("/predict", methods=["POST"])
def predict():
    try:
        if model is None:
            raise Exception("Model not loaded")

        data = request.get_json()
        logging.info(f"Input received: {data}")

        # Convert JSON dict to DataFrame
        df = pd.DataFrame([data["features"]])

        pred = model.predict(df)
        return jsonify({"prediction": float(pred[0])})

    except Exception as e:
        logging.error(f"Prediction failed: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
