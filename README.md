# Manufacturing Predictive Maintenance using Machine Learning

This project demonstrates a predictive maintenance system for manufacturing equipment using a machine learning model.  
The model predicts whether a machine is likely to fail based on sensor input parameters.

---

## Project Overview
Unexpected machine failures can cause production downtime and financial loss.  
This project uses a trained Random Forest machine learning model to predict machine failure using historical manufacturing sensor data.

---

## Files in the Repository
- `predict.py` – Python script to load the trained model and predict machine failure
- `random_forest_model.pkl` – Trained Random Forest machine learning model
- `scaler.pkl` – Feature scaler used during model training

---

## Input Parameters
The model takes the following machine sensor values as input:
- Air Temperature
- Process Temperature
- Rotational Speed
- Torque
- Tool Wear

---

## Output
- **Machine Failure Predicted**
- **No Machine Failure**

---

## How to Run the Project
1. Install required Python libraries:
   ```bash
   pip install pandas scikit-learn joblib
   python predict.py
