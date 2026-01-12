# app/app.py

from fastapi import FastAPI
from pydantic import BaseModel
from .logger import log_prediction  # Import the function from logger.py

# Create FastAPI instance
app = FastAPI()

# Define input schema using Pydantic
class InputData(BaseModel):
    feature1: float
    feature2: float

# Root endpoint
@app.get("/")
def read_root():
    """
    Simple root endpoint to check if API is running.
    """
    return {"message": "api success"}

# Prediction endpoint
@app.post("/predict")
def predict(data: InputData):
    """
    Receives JSON input like:
    {
        "feature1": 10,
        "feature2": 5
    }

    Calls log_prediction from logger.py and returns prediction.
    """
    # Convert Pydantic model to dict
    input_dict = data.dict()
    
    # Get prediction from logger
    result = log_prediction(input_dict)
    
    return result
