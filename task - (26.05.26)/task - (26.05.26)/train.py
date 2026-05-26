# ============================================================
#        ENSEMBLE LEARNING - DIABETES PREDICTION
#        train.py — Training, Evaluation & Model Saving
# ============================================================

# -- Imports --------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os
import warnings
warnings.filterwarnings("ignore")

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

from sklearn.ensemble import (
    RandomForestClassifier,
    AdaBoostClassifier,
    GradientBoostingClassifier,
    BaggingClassifier
)
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier


# ============================================================
# SECTION 1 — DATA LOADING
# ============================================================
print("=======================================================")
print("  ENSEMBLE LEARNING — DIABETES PREDICTION TRAINING")
print("=======================================================")

df = pd.read_csv("./data/diabetes.csv")

print("\n[INFO] Dataset Shape:", df.shape)
print("\n[INFO] First 5 Rows:")
print(df.head())
print("\n[INFO] Basic Statistics:")
print(df.describe())
print("\n[INFO] Missing Values Summary:")
print(df.isnull().sum())


# ============================================================
# SECTION 2 — DATA PREPROCESSING
# ============================================================
print("\n\n-------------------------------------------------------")
print("SECTION 2: DATA PREPROCESSING")
print("-------------------------------------------------------")

# Replace 0s with NaN for biologically impossible values
cols_with_zeros = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
df[cols_with_zeros] = df[cols_with_zeros].replace(0, np.nan)

# Fill NaN with median
df.fillna(df.median(), inplace=True)

print("[STATUS] Zero values successfully replaced with feature medians.")
print("[STATUS] Missing values handled.")

# Features & Target
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

# Train-Test Split (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

print(f"[INFO] Training set size: {X_train.shape[0]} samples")
print(f"[INFO] Testing set size: {X_test.shape[0]} samples")


# ============================================================
# SECTION 3 — MAIN MODEL TRAINING (RANDOM FOREST)
# ============================================================
print("\n\n-------------------------------------------------------")
print("SECTION 3: RANDOM FOREST MODEL INITIALIZATION")
print("-------------------------------------------------------")

rf_model = RandomForestClassifier(
    n_estimators=100,
    max_depth=6,
    random_state=42
)
rf_model.fit(X_train_scaled, y_train)
rf_pred = rf_model.predict(X_test_scaled)
rf_acc  = accuracy_score(y_test, rf_pred)

print(f"\n[METRIC] Random Forest Accuracy: {rf_acc * 100:.2f}%")
print("\n[METRIC] Classification Report:")
print(classification_report(y_test, rf_pred))


# ============================================================
# SECTION 4 — ALGORITHM BENCHMARK COMPARISON
# ============================================================
print("\n\n-------------------------------------------------------")
print("SECTION 4: FRAMEWORK BENCHMARK COMPARISON")
print("-------------------------------------------------------")

models = {
    "Decision Tree"       : DecisionTreeClassifier(random_state=42),
    "Logistic Regression" : LogisticRegression(random_state=42),
    "KNN"                 : KNeighborsClassifier(),
    "Bagging"             : BaggingClassifier(random_state=42),
    "AdaBoost"            : AdaBoostClassifier(random_state=42),
    "Gradient Boosting"   : GradientBoostingClassifier(random_state=42),
    "Random Forest"       : rf_model,
}

results = {}
print(f"\n{'Model Architecture':<25} {'Accuracy':>10}")
print("-" * 37)

for name, model in models.items():
    if name != "Random Forest":
        model.fit(X_train_scaled, y_train)
    pred = model.predict(X_test_scaled)
    acc  = accuracy_score(y_test, pred)
    results[name] = round(acc * 100, 2)
    print(f"{name:<25} {acc * 100:>9.2f}%")


# ============================================================
# SECTION 5 — SERIALIZATION & EXPORT
# ============================================================
print("\n\n-------------------------------------------------------")
print("SECTION 5: PIPELINE SERIALIZATION")
print("-------------------------------------------------------")

os.makedirs("model", exist_ok=True)

# Save Random Forest model
joblib.dump(rf_model, "model/random_forest.pkl")

# Save scaler
joblib.dump(scaler, "model/scaler.pkl")

print("[EXPORT] Random Forest model exported to: model/random_forest.pkl")
print("[EXPORT] Training scaler pipeline exported to: model/scaler.pkl")
print("\n[COMPLETE] Model training and preprocessing initialization ended successfully.")