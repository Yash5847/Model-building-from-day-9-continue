# 📅 Day 17: Model Monitoring & Prediction Logging

## 🎯 Objective
To implement model monitoring by logging predictions along with input data and timestamps, enabling tracking of model behavior in a production-like environment.

---

## 🛠️ What Was Implemented

- Loaded the trained machine learning model
- Logged model predictions automatically
- Stored:
  - Prediction timestamp
  - Input features
  - Model output
- Created a monitoring pipeline to support future:
  - Data drift detection
  - Model retraining
  - Performance tracking

---

## 📂 Files & Folder Structure

ML_Project/
├── models/
│ └── best_model.pkl
├── data/
│ └── sample_input.csv
├── logs/
│ └── prediction_logs.csv
├── src/
│ ├── monitor.py
│ └── test_monitor.py

yaml
Copy code

---

## 📄 File Description

### `monitor.py`
- Loads the trained model
- Performs predictions
- Logs predictions with timestamps into a CSV file

### `test_monitor.py`
- Sends sample input data to the monitoring pipeline
- Verifies prediction logging functionality

### `prediction_logs.csv`
- Stores real-time prediction logs
- Acts as monitoring data for production analysis

---

## 🔁 Monitoring Workflow

sample_input.csv
↓
monitor.py
↓
best_model.pkl
↓
prediction
↓
prediction_logs.csv

yaml
Copy code

---

## ✅ Outcome

- Model predictions are successfully logged
- Monitoring pipeline works without errors
- Project now includes a production-ready ML lifecycle component

---

## 🧠 Key Learning

> Deployment is not the final step — continuous monitoring is essential to ensure model reliability and performance over time.

---

## 🚀 Next Steps

- Detect data drift using logged predictions
- Implement automated model retraining
- Add alerting and performance metrics