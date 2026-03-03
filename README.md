# 🚀 Customer Churn Prediction App

A Machine Learning web application that predicts whether a customer is likely to churn based on user inputs.

## 🌐 Live Demo
🔗 **Live Application:**  
[🚀 (https://ml-customer-churn-prediction-app.streamlit.app)]
---

## 📌 Project Overview

This project uses a trained classification model to predict customer churn.  
Users can input:

- Age  
- Tenure  
- Monthly Charges  
- Gender  

The app processes the input, scales the data, and generates a real-time churn prediction.

---

## 🛠 Tech Stack

- Python
- Streamlit
- Scikit-learn
- NumPy
- Pandas
- Pickle (for model & scaler serialization)

---

## ⚙️ How It Works

1. User enters input values in the Streamlit UI.
2. Input is converted into a NumPy array.
3. Data is scaled using a saved scaler (`scaler.pkl`).
4. Trained ML model (`best_model.pkl`) makes prediction.
5. App displays result instantly.

---

## 🧠 Machine Learning Model

- Classification Model
- Preprocessed using feature scaling
- Trained to predict customer churn (Yes / No)

---

## 📂 Project Structure
