import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.monitor import predict_and_log

sample_input = pd.read_csv("data/sample_input.csv")

predict_and_log(sample_input.head(1))

