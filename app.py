#Gender -> 1 for female and 0 for male
#Churn -> 1 for 'Yes' and 0 for 'No'

#Scaler is imported as scaler.pkl and model is imported as model.pkl

 #order of x -> ['Age', 'Gender', 'Tenure', 'MonthlyCharges']

import streamlit as st
import numpy as np
import joblib

scaler = joblib.load('scaler.pkl')  # Load the fitted scaler object from the file 'scaler.pkl' using joblib's load function
model = joblib.load('best_model.pkl')      # Load the trained model from the file '


st.title("Customer Churn Prediction")

st.divider()

st.write("Please enter the values and hit the predict button for getting a prediction.")

st.divider()

age = st.number_input("Enter your Age", min_value=10, max_value=100, value=30)     # Create a number input field for the user's age, allowing values between 10 and 100, with a default value of 30
tenure = st.number_input("Enter your Tenure", min_value=0, max_value=130, value=10) # Create a number input field for the user's tenure, allowing values between 0 and 130, with a default value of 10
monthly_charges = st.number_input("Enter your Monthly Charges", min_value=0, max_value=1000, value=150) # Create a number input field for the user's monthly charges, allowing values between 0.0 and 1000.0, with a default value of 50.0
gender = st.selectbox("Select your Gender", options=["Female", "Male"]) # Create a select box for the user's gender, with options 

st.divider()

predict_button = st.button("Predict")  # Create a button labeled "Predict" and store its state (clicked or not) in the variable predict_button

st.divider()

if predict_button:  # Check if the predict button was clicked

    gender_selected = 1 if gender == "female" else 0  # Convert the selected
    x = [age, gender_selected, tenure, monthly_charges]  # Create a list of the input features in the correct order
    x = np.array(x)
    x_array = scaler.transform([x])


    prediction = model.predict(x_array)[0]

    predicted = "YES" if prediction == 1 else "NO"
    st.balloons()

    st.write(f"predicted: {predicted}")
else:
    st.write("Please enter the values and hit the predict button for getting a prediction.")    
