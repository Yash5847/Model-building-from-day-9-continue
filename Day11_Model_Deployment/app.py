import streamlit as st
import joblib
import pandas as pd

# Load trained pipeline
model = joblib.load("bigmart_sales_model.pkl")

st.title("BigMart Sales Prediction App")

# --------------------
# User Inputs
# --------------------
item_identifier = st.text_input("Item Identifier", "FDA15")  # placeholder default
item_weight = st.number_input("Item Weight", min_value=0.0, step=0.1)
item_fat = st.selectbox("Item Fat Content", ["Low Fat", "Regular"])
item_visibility = st.number_input("Item Visibility", min_value=0.0, step=0.001)
item_mrp = st.number_input("Item MRP", min_value=0.0, step=0.1)
item_type = st.text_input("Item Type", "Dairy")  # placeholder default
outlet_identifier = st.text_input("Outlet Identifier", "OUT049")  # placeholder default
outlet_establishment_year = st.number_input("Outlet Establishment Year", min_value=1900, step=1)
outlet_size = st.selectbox("Outlet Size", ["Small", "Medium", "High"])
outlet_location_type = st.selectbox("Outlet Location Type", ["Tier 1", "Tier 2", "Tier 3"])
outlet_type = st.text_input("Outlet Type", "Supermarket Type1")  # placeholder default

# --------------------
# Prediction
# --------------------
if st.button("Predict Sales"):
    input_df = pd.DataFrame({
        "Item_Identifier": [item_identifier],
        "Item_Weight": [item_weight],
        "Item_Fat_Content": [item_fat],
        "Item_Visibility": [item_visibility],
        "Item_MRP": [item_mrp],
        "Item_Type": [item_type],
        "Outlet_Identifier": [outlet_identifier],
        "Outlet_Establishment_Year": [outlet_establishment_year],
        "Outlet_Size": [outlet_size],
        "Outlet_Location_Type": [outlet_location_type],
        "Outlet_Type": [outlet_type]
    })

    prediction = model.predict(input_df)
    st.success(f"Predicted Sales: ₹ {prediction[0]:.2f}")
