# ML Project - Sales Prediction API

This project is a Machine Learning API built using Flask.  
It predicts sales using a trained RandomForestRegressor model.

Project Structure:

ML_Project/
  ├─ app/
  │   ├─ app.py
  │   ├─ __init__.py
  │   ├─ logger.py
  │   └─ logs/
  ├─ models/
  │   ├─ best_model.pkl
  │   └─ model.pkl
  ├─ notebooks/
  ├─ src/
  ├─ requirements.txt
  └─ README.md


How to Run:

1. Install dependencies:

pip install -r requirements.txt

2. Start the Flask API:

cd app
python app.py

3. Test API:

Invoke-RestMethod `
  -Uri http://127.0.0.1:5000/predict `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"features":{"Item_Weight":4,"Item_Fat_Content":128,"Item_Visibility":6,"Item_Type":1,"Item_MRP":250,"Outlet_Identifier":1,"Outlet_Size":2,"Outlet_Location_Type":2,"Outlet_Type":1,"Outlet_Years":5}}'


Input Features:

The model expects 10 features:

- Item_Weight
- Item_Fat_Content
- Item_Visibility
- Item_Type
- Item_MRP
- Outlet_Identifier
- Outlet_Size
- Outlet_Location_Type
- Outlet_Type
- Outlet_Years


Output:

The API returns:

{
  "prediction": <sales_value>
}

Notes:

- Ensure best_model.pkl is present in the models/ folder.
- API runs on http://127.0.0.1:5000/
