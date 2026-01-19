MLOps Project – Drift Detection and Automated Retraining

This project demonstrates an end-to-end MLOps workflow including model prediction, drift detection, monitoring, and automated retraining triggered by drift reports.

Project Overview

The objective of this project is to ensure that a deployed machine learning model remains reliable over time. This is achieved by continuously monitoring incoming data, detecting drift, and retraining the model whenever drift is observed.

Project Structure

project
│
├── app.py
├── model.pkl
├── requirements.txt
│
├── src
│ ├── predict.py
│ ├── monitor.py
│ ├── drift_prediction.py
│ ├── test_monitor.py
│ └── other source files
│
├── reports
│ └── drift_report.html
│
├── retraining
│ ├── trigger.py
│ └── retrain.py
│
└── README.md

Drift Detection and Monitoring (Day 18–19)

Drift detection is implemented inside the src module.
Evidently is used to detect data drift and generate a drift report.
The drift report is saved as an HTML file for analysis and validation.

Output file:
reports/drift_report.html

Automated Retraining Pipeline (Day 22)

An automated retraining pipeline is implemented to handle model degradation.

Key points:

Drift detection is performed first

Once a drift report is generated, retraining is triggered

The pipeline reloads data, preprocesses it, retrains the model, and saves the updated model

Relevant files:
retraining/trigger.py
retraining/retrain.py

How Retraining Works

If a drift report exists in the reports directory, the retraining pipeline is executed.
If no drift is detected, retraining is skipped.

This completes the monitoring-to-retraining feedback loop.

Testing

Monitoring and drift logic is validated using test files present in the src directory.

Tools and Technologies

Python
Scikit-learn
Evidently
Flask
Git and GitHub

Key Learnings

Model monitoring is essential after deployment
Drift detection helps identify performance issues early
Automated retraining ensures long-term model reliability