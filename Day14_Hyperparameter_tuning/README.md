# Day 14 – Hyperparameter Tuning & Model Optimization

## Project Overview
This project focuses on improving machine learning model performance using hyperparameter tuning techniques. GridSearchCV is applied to a Random Forest Regressor to identify the best combination of parameters using cross-validation on the BigMart Sales dataset.

---

## Objectives
- Understand hyperparameters vs model parameters
- Apply GridSearchCV for model optimization
- Improve model performance using cross-validation
- Evaluate model using R² Score and RMSE
- Save the optimized model for future use

---

## Project Structure
Day_14_Hyperparameter_Tuning/
│
├── data/
│   └── BigMartSales.csv
│
├── notebooks/
│   └── Day_14_Hyperparameter_Tuning.ipynb
│
├── models/
│   └── best_model.pkl
│
└── README.md

---

## Concepts Covered
- Hyperparameter Tuning
- GridSearchCV
- Cross-Validation
- Random Forest Regressor
- Model Evaluation
- Model Persistence using Joblib

---

## Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Jupyter Notebook (VS Code)

---

## Workflow
1. Load the BigMart Sales dataset
2. Split data into features and target
3. Perform train-test split
4. Define Random Forest Regressor
5. Create hyperparameter grid
6. Apply GridSearchCV with 5-fold cross-validation
7. Select best model
8. Evaluate model using R² Score and RMSE
9. Save the optimized model

---

## Model Evaluation
- R² Score is used to measure how well the model explains variance
- RMSE is used to measure prediction error

Note: Evaluation scores may vary based on parameter tuning and data preprocessing.

---

## Model Saving
The best performing model is saved using joblib at:

models/best_model.pkl

This model can be reused for deployment or further predictions.

---

## Outcome
- Improved model performance
- Best hyperparameters identified
- Industry-standard ML workflow followed
- Optimized model saved successfully

---

## Next Steps
- Feature Importance and Model Explainability
- Model Deployment using Flask or FastAPI

---

## Author
Yash Desai  

