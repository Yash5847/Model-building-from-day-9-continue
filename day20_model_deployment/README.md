# Day 20 – Machine Learning Model Deployment

This project demonstrates an end-to-end machine learning deployment workflow
using FastAPI and Streamlit.

A trained machine learning model is serialized and exposed as a REST API using
FastAPI, and predictions are consumed through a Streamlit-based web interface.

---

## 📁 Project Structure

day20_model_deployment/
│
├── backend/
│   └── api.py          # FastAPI backend
│
├── frontend/
│   └── app.py          # Streamlit frontend
│
├── model/
│   └── model.pkl       # Saved ML model
│
├── save_model.py       # Script to train and save 
└── README.md

---

## 🛠 Tech Stack

- Python 3.7
- Scikit-learn
- FastAPI
- Uvicorn
- Streamlit

---

## 🔄 Workflow

1. Train a machine learning model offline.
2. Save the trained model using Pickle.
3. Load the model in a FastAPI backend.
4. Expose predictions through a REST API.
5. Consume the API using a Streamlit frontend.

---

## ▶️ How to Run

### 1️⃣ Install Dependencies
pip install -r requirements.txt


2️⃣ Train & Save Model
python save_model.py


3️⃣ Run Backend
cd backend
uvicorn api:app --reload
Backend URL:
http://127.0.0.1:8000/docs


4️⃣ Run Frontend
Open a new terminal:
cd frontend
streamlit run app.py

Frontend URL:
http://localhost:8501

🧪 Sample Input

{
  "features": [1, 2, 3]
}

✅ Output
The application returns a prediction from the deployed machine learning model
and displays it on the Streamlit UI.

![alt text](<Screenshot 2026-01-16 194911.png>) ![alt text](<Screenshot 2026-01-16 194927.png>)