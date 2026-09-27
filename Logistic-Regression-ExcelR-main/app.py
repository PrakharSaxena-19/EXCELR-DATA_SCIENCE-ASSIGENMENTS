import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Diabetes Prediction", page_icon="🩺")

st.title("Diabetes Prediction using Logistic Regression")
st.write("Enter the patient details below to predict the diabetes outcome.")

model = joblib.load("logistic_regression_model.pkl")

Pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
Glucose = st.number_input("Glucose", min_value=0, max_value=250, value=120)
BloodPressure = st.number_input("BloodPressure", min_value=0, max_value=150, value=70)
SkinThickness = st.number_input("SkinThickness", min_value=0, max_value=100, value=20)
Insulin = st.number_input("Insulin", min_value=0, max_value=900, value=80)
BMI = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
DiabetesPedigreeFunction = st.number_input(
    "DiabetesPedigreeFunction", min_value=0.0, max_value=3.0, value=0.47
)
Age = st.number_input("Age", min_value=1, max_value=120, value=30)

if st.button("Predict"):
    input_data = pd.DataFrame([{
        "Pregnancies": Pregnancies,
        "Glucose": Glucose,
        "BloodPressure": BloodPressure,
        "SkinThickness": SkinThickness,
        "Insulin": Insulin,
        "BMI": BMI,
        "DiabetesPedigreeFunction": DiabetesPedigreeFunction,
        "Age": Age
    }])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("Prediction: The model predicts a positive diabetes outcome.")
    else:
        st.success("Prediction: The model predicts a negative diabetes outcome.")
