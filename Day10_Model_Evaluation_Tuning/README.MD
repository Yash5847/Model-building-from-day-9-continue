# Day 10: Model Evaluation & Hyperparameter Tuning (BigMart Sales)

## 📌 Objective
To evaluate machine learning models and improve prediction performance on the BigMart Sales dataset using proper preprocessing, model comparison, and hyperparameter tuning.

---

## 📂 Dataset
**BigMartSales.csv**

Target Variable:
- `Item_Outlet_Sales`

---

## 🔧 Steps Performed

### 1. Data Loading
- Loaded the BigMart Sales dataset using Pandas.

### 2. Data Preprocessing
- Removed identifier column (`Item_Identifier`) as it does not contribute to prediction.
- Converted categorical variables into numerical format using **One-Hot Encoding**.
- Verified that no string (`object`) data types remained.

### 3. Feature & Target Separation
- Features (`X`) and target (`y`) were defined after encoding.

### 4. Train-Test Split
- Split the data into 80% training and 20% testing sets.

### 5. Model Training
- Trained the following models:
  - Linear Regression
  - Random Forest Regressor

### 6. Model Evaluation
- Evaluated models using:
  - R² Score
  - Mean Absolute Error (MAE)
  - Root Mean Squared Error (RMSE)

### 7. Hyperparameter Tuning
- Applied **GridSearchCV** on Random Forest to find optimal parameters.
- Selected the best-performing model based on R² score.

---

## 🧪 Tools & Libraries Used
- Python
- Pandas
- NumPy
- Scikit-learn

---

## ✅ Outcome
- Linear Regression served as a baseline model.
- Tuned Random Forest Regressor achieved better predictive performance.
- Final model selected after hyperparameter tuning.

---

## 📘 Key Learning
- Machine learning models require numerical input.
- Identifier columns should be removed to avoid noise.
- Proper preprocessing before train-test split is crucial.
- Hyperparameter tuning significantly improves model performance.
