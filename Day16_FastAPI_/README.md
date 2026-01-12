# Day 16 - FastAPI ML API

This project demonstrates how to build a **FastAPI application** to serve machine learning predictions.  
It includes a `/predict` endpoint that accepts JSON input and returns a prediction. Currently, it uses a **dummy prediction function** (sum of input features) to test the API.

---

## Folder Structure

Day16_FastAPI_ML/
│
├─ app/
│ ├─ init.py # Required for Python package
│ ├─ app.py # FastAPI application
│ └─ logger.py # Handles model loading and prediction
│
├─ models/
│ └─ best_model.pkl # Optional trained ML model
│
├─ requirements.txt # Python dependencies
└─ README.md

yaml
Copy code

---

## Installation

1. Clone the repository:

```bash
git clone <your-github-repo-url>
cd Day16_FastAPI_ML
(Optional) Create a virtual environment:

bash
Copy code
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Running the API
Start the FastAPI server:

bash
Copy code
uvicorn app.app:app --reload
The server will run at http://127.0.0.1:8000/

Swagger UI (interactive API documentation) is available at http://127.0.0.1:8000/docs

Endpoints
1. GET /
Checks if the API is running.

Example Response:

json
Copy code
{
  "message": "api success"
}
2. POST /predict
Accepts JSON input with features and returns a prediction.

Current dummy function returns sum of input features. Replace logger.py with a real ML model for actual predictions.

Request Example:

json
Copy code
{
  "feature1": 10,
  "feature2": 5
}
Response Example:

json
Copy code
{
  "prediction": 15
}
Another Example:

json
Copy code
{
  "feature1": 7,
  "feature2": 3
}
Response:

json
Copy code
{
  "prediction": 10
}
Notes
Make sure best_model.pkl exists in the models/ folder if you want real predictions.

Tested on Python 3.7+.

Use Swagger UI for easy testing of endpoints.

