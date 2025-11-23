# 🚗 Car Safety Predictor

A beginner-friendly machine learning web application that predicts whether a car is **Safe** or **Not Safe** based on its essential features. This project uses the UCI Car Evaluation dataset and a Logistic Regression model to classify vehicle safety.

---

## ✨ Overview

This project helps users understand how different car attributes influence safety ratings. By selecting key features such as buying price, maintenance cost, and seating capacity, the app instantly predicts whether a car is safe.

### Key Features
- **Instant Safety Prediction** using a trained ML model  
- **Easy-to-Use Streamlit Interface**  
- **Beginner-Friendly Implementation**  
- **End-to-End ML Workflow** (data preprocessing → model training → deployment)

---

## 🎯 Why This Project?

- Uses a **real-world dataset** widely applied in ML education  
- Demonstrates a complete **ML pipeline with deployment**  
- Helps beginners understand classification using Logistic Regression  
- Shows how car attributes influence safety decisions  

---

## 🛠️ Tech Stack

- **Machine Learning:** Python, Scikit-Learn  
- **Data Processing:** Pandas, NumPy  
- **Web App Framework:** Streamlit  
- **Model Saving:** Joblib  

---

## 🔄 Workflow

1. **Load & Inspect Dataset**  
2. **Preprocess Data**  
   - One-hot encode categorical features  
   - Convert target into binary (1 = Safe, 0 = Not Safe)  
3. **Train Logistic Regression Model**  
4. **Evaluate Model Performance**  
5. **Save Artifacts:**  
   - `car_safety_model.pkl`  
   - `car_safety_scaler.pkl`  
   - `car_safety_feature_columns.pkl`  
6. **Deploy using Streamlit**  

---

## 📊 Dataset

This project uses the **UCI Car Evaluation Dataset**.

### Features
- Buying Price: `vhigh`, `high`, `med`, `low`  
- Maintenance Cost: `vhigh`, `high`, `med`, `low`  
- Number of Doors: `2`, `3`, `4`, `5more`  
- Passenger Capacity: `2`, `4`, `more`  
- Luggage Size: `small`, `med`, `big`  
- **Target:** Safe / Not Safe  

### Source  
UCI ML Repository – Car Evaluation Dataset  

---

## 📁 Project Structure
- app.py
- Car_Safety_Predicton.ipynb
- car_safety_model.pkl
- car_safety_scaler.pkl
- car_safety_feature_columns.pkl
- car_data.csv
- README.md

---

## ⚠️ Disclaimer

This project is intended **for educational purposes only**.  
Predictions are based on patterns learned from the dataset and should not be considered official car safety ratings. Refer to certified automotive safety authorities for real-world decisions.

---
