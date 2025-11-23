import streamlit as st
import pandas as pd
import joblib
st.title("Car Safety Predictor")
st.write("Enter car details below to check if it's predicted to be SAFE or NOT SAFE.")
model = joblib.load("car_safety_model.pkl")
scaler = joblib.load("car_safety_scaler.pkl")
feature_cols = joblib.load("car_safety_feature_columns.pkl")
buying = st.selectbox("Buying Price", ["vhigh", "high", "med", "low"])
maint = st.selectbox("Maintenance Cost", ["vhigh", "high", "med", "low"])
doors = st.selectbox("Number of Doors", ["2", "3", "4", "5more"])
persons = st.selectbox("Persons Capacity", ["2", "4", "more"])
lug_boot = st.selectbox("Luggage Size", ["small", "med", "big"])
input_data = pd.DataFrame({
    'buying': [buying],
    'maint': [maint],
    'doors': [doors],
    'persons': [persons],
    'lug_boot': [lug_boot]
})
st.write("You entered:")
st.write(input_data)
input_encoded = pd.get_dummies(input_data)
input_encoded = input_encoded.reindex(columns=feature_cols, fill_value=0)
input_scaled = scaler.transform(input_encoded)
if st.button("Predict Safety"):
    pred = model.predict(input_scaled)[0]
    prob = model.predict_proba(input_scaled)[0][1]
    st.write("---")
    if pred == 1:
        st.success(f"Safe (chance: {prob:.2f})")
    else:
        st.error(f"Not Safe (chance: {prob:.2f})")
    st.write(f"Probability of Safe: {prob:.2f}")