import pandas as pd
import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.monitor import predict_and_log

# Load sample input CSV
sample_input = pd.read_csv("data/sample_input.csv")

# Predict and log
predict_and_log(sample_input.head(1))
