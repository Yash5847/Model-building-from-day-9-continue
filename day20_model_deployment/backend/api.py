from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import pickle

app = FastAPI()

with open("../model/model.pkl", "rb") as f:
    model = pickle.load(f)

class InputData(BaseModel):
    features: List[float]

@app.get("/")
def home():
    return {"status": "API running"}

@app.post("/predict")
def predict(data: InputData):
    prediction = model.predict([data.features])
    return {"prediction": int(prediction[0])}
