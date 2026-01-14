import pandas as pd
from monitor import predict_and_log

sample_input = pd.read_csv("../data/sample_input.csv")

prediction = predict_and_log(sample_input.head(1))

print("Prediction:", prediction)
print("Logged successfully!")
