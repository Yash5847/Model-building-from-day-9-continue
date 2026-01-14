## Day 18 – Model Monitoring

### Objective
To implement a basic model monitoring system that tracks live predictions, input data, and timestamps to simulate a production ML environment.

---

### What Was Implemented
- Loaded trained ML model for inference
- Simulated real-time prediction using sample input data
- Logged:
  - Input features
  - Model predictions
  - Prediction timestamp
- Stored logs in a CSV file for monitoring and analysis

---

### Folder Structure
ML_Project/
├── data/
│ ├── BigMartSales.csv
│ └── sample_input.csv
├── models/
│ └── model.pkl
├── logs/
│ └── predictions_log.csv
├── src/
│ ├── monitor.py
│ └── test_monitor.py
└── README.md

---

### Key Files
- `monitor.py`  
  Handles prediction and logging logic.
- `test_monitor.py`  
  Simulates real-time inference using sample data.
- `predictions_log.csv`  
  Stores prediction logs with timestamps.

---

### How to Run
```bash
cd src
python test_monitor.py
Output
Terminal displays model prediction

logs/predictions_log.csv is created/updated with:

Input data

Prediction

Timestamp

Outcome
This setup forms the foundation for:

Model performance tracking

Data drift detection

Automated retraining pipelines

Production-grade ML monitoring