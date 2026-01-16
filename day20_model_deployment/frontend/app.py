import streamlit as st
import requests

st.title("Day 20 – ML Model Deployment")

f1 = st.number_input("Feature 1")
f2 = st.number_input("Feature 2")
f3 = st.number_input("Feature 3")

if st.button("Predict"):
    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json={"features": [f1, f2, f3]}
    )

    if response.status_code == 200:
        result = response.json()
        st.success(f"Prediction: {result['prediction']}")
    else:
        st.error(f"API Error: {response.text}")
