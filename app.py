import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the saved model
model = joblib.load('models/fraud_model.pkl')

# App title
st.title('💳 Credit Card Fraud Detection System')
st.write('Enter transaction details below to predict if it is fraudulent or not.')

# Input fields
st.subheader('Transaction Details')

amount = st.number_input('Transaction Amount ($)', min_value=0.0, value=100.0)

st.write('Enter V1 to V28 feature values (from the dataset):')

v_features = []
for i in range(1, 29):
    v = st.number_input(f'V{i}', value=0.0)
    v_features.append(v)

# Scale the amount
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
amount_scaled = scaler.fit_transform([[amount]])[0][0]

# Combine all features
input_data = np.array([v_features + [amount_scaled]])

# Predict button
if st.button('🔍 Predict'):
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    if prediction[0] == 1:
        st.error('🚨 FRAUDULENT TRANSACTION DETECTED!')
        st.write(f'Fraud Probability: {probability[0][1]*100:.2f}%')
    else:
        st.success('✅ Transaction appears NORMAL')
        st.write(f'Fraud Probability: {probability[0][1]*100:.2f}%')