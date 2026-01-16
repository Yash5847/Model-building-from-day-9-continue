import pickle
from sklearn.linear_model import LogisticRegression

X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = [0, 1, 1]

model = LogisticRegression()
model.fit(X, y)

with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("model.pkl saved successfully")
