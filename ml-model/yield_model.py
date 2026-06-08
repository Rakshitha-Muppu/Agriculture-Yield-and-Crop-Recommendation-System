import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score

# Load dataset
df = pd.read_csv("../dataset/yield_prediction.csv")

print("Original Shape:", df.shape)

# Remove rows with missing values
df = df.dropna()

print("Shape After Cleaning:", df.shape)

# Check if any missing values remain
print("\nMissing Values:")
print(df.isnull().sum())

# Encode categorical columns
encoders = {}

categorical_cols = [
    "State_Name",
    "District_Name",
    "Season",
    "Crop"
]

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    encoders[col] = le

# Features
X = df[
    [
        "State_Name",
        "District_Name",
        "Crop_Year",
        "Season",
        "Crop",
        "Temperature",
        "Humidity",
        "Soil_Moisture",
        "Area"
    ]
]

# Target
y = df["Production"]

print("\nNaN in Features:", X.isnull().sum().sum())
print("NaN in Target:", y.isnull().sum())

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestRegressor(
    n_estimators=20,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation
score = r2_score(y_test, predictions)

print("\nR2 Score:", score)

# Save model
with open("yield_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save encoders
with open("yield_encoders.pkl", "wb") as f:
    pickle.dump(encoders, f)

print("\nYield model saved successfully!")
print("Encoder file saved successfully!")