

import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load Model
model = joblib.load("fraud_model.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Credit Card Fraud Detection System")

st.write("Enter transaction details below")

# Input Features
time = st.number_input("Time", value=0.0)
amount = st.number_input("Amount", value=0.0)

features = []

for i in range(1, 29):
    val = st.number_input(f"V{i}", value=0.0)
    features.append(val)

if st.button("Detect Fraud"):

    data = [[time] + features + [amount]]

    data_scaled = scaler.transform(data)

    prediction = model.predict(data_scaled)

    if prediction[0] == 1:
        st.error("⚠ Fraudulent Transaction Detected")
    else:
        st.success("✅ Legitimate Transaction")