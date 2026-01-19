import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

# Load datasets
reference_data = pd.read_csv("data/reference_data.csv")
current_data = pd.read_csv("data/current_data.csv")

# Create drift report
drift_report = Report(
    metrics=[
        DataDriftPreset()
    ]
)

# Run drift detection
drift_report.run(
    reference_data=reference_data,
    current_data=current_data
)


drift_report.save_html("reports/drift_report.html")

print("✅ Data Drift Report Generated Successfully!")
