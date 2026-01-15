import pandas as pd
import numpy as np

np.random.seed(42)

reference_data = pd.DataFrame({
    "age": np.random.randint(20, 60, 200),
    "salary": np.random.randint(30000, 80000, 200),
    "experience": np.random.randint(1, 20, 200)
})

current_data = pd.DataFrame({
    "age": np.random.randint(25, 65, 200),
    "salary": np.random.randint(35000, 100000, 200),
    "experience": np.random.randint(2, 25, 200)
})

reference_data.to_csv("data/reference_data.csv", index=False)
current_data.to_csv("data/current_data.csv", index=False)

print("✅ reference_data.csv and current_data.csv created successfully")

