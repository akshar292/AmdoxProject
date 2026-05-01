import streamlit as st
import requests

st.title("🛒 NeuralRetail Dashboard")

st.header("Demand Prediction")

price = st.number_input("Price", value=100)
promo = st.selectbox("Promo Flag", [0, 1])
season = st.number_input("Season (month)", value=5)

if st.button("Predict Demand"):

    url = "http://127.0.0.1:8000/predict/demand"

    payload = {
        "price": price,
        "promo_flag": promo,
        "season": season
    }

    try:
        res = requests.post(url, json=payload)

        if res.status_code == 200:
            st.success(f"Predicted Demand: {res.json()}")
        else:
            st.error("API Error")

    except Exception as e:
        st.error(f"Connection Error: {e}")