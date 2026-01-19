import os

DRIFT_REPORT_PATH = "reports/drift_report.html"

def should_retrain():
    """
    If drift report exists, assume drift detected.
    """
    return os.path.exists(DRIFT_REPORT_PATH)
