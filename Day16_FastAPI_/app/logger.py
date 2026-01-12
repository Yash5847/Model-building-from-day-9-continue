import pickle
import os

# Path to your trained model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "../models/best_model.pkl")

# Load the model once when the API starts
try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    model = None
    print(f"Error: Model file not found at {MODEL_PATH}")
except Exception as e:
    model = None
    print(f"Error loading model: {e}")


def log_prediction(input_data):
    """
    Returns prediction from the trained model.
    
    input_data: dict, e.g., {"feature1": 10, "feature2": 5}
    """
    if model is None:
        return {"error": "Model not loaded"}
    
    try:
        # Convert input dict to list of features (model expects 2D array)
        features = [list(input_data.values())]  # shape: [[feature1, feature2, ...]]
        
        # Get prediction
        prediction = model.predict(features)
        
        # Return as JSON
        return {"prediction": float(prediction[0])}  # convert numpy type to float for JSON
    except Exception as e:
        return {"error": str(e)}
