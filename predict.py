import joblib
import pandas as pd

model = joblib.load("random_forest_model.pkl")
scaler = joblib.load("scaler.pkl")

columns = [
    "Air_Temperature",
    "Process_Temperature",
    "Rotational_Speed",
    "Torque",
    "Tool_Wear"
]

new_values = [[295, 310, 1400, 30, 40]]

data = pd.DataFrame(new_values, columns=columns)
data = scaler.transform(data)

result = model.predict(data)

if result[0] == 1:
    print("Machine Failure Predicted")
else:
    print("No Machine Failure")
