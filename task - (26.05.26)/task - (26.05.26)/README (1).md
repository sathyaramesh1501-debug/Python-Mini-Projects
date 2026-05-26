<h1 align="center">Random Forest Model</h1>

<p align="center">Diabetes prediction with ensemble learning (Pima Indians dataset) · Streamlit demo</p>

---

## Introduction

This project predicts diabetes risk using a **Random Forest** classifier trained on the Pima Indians Diabetes dataset. It compares several sklearn models, saves the trained forest and a **StandardScaler**, and ships a **Streamlit** app where you enter patient features and see risk output plus a benchmark table.

---

## Setup

1. Open a terminal in this project folder (the folder that contains `app.py`, `train.py`, and `data/`).

2. Create a virtual environment (recommended):

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. **Train** (creates `model/random_forest.pkl` and `model/scaler.pkl`):

   ```bash
   python train.py
   ```

5. **Run the demo app**:

   ```bash
   streamlit run app.py
   ```

Dependencies were captured with `pip freeze > requirements.txt` so your environment matches what was used for development.

---

## Folder structure

```
Task (26-05-2026)/
├── app.py                 # Streamlit UI and predictions
├── train.py               # Preprocess, train, benchmark, save artifacts
├── requirements.txt       # Pinned dependencies (pip freeze)
├── README.md
├── Ensemble_Learning_Theory.pdf
├── data/
│   └── diabetes.csv       # Dataset
├── model/
│   ├── random_forest.pkl  # Trained classifier (after train.py)
│   └── scaler.pkl         # Fitted StandardScaler (after train.py)
└── Screenshots/
    ├── screenshot 1.png
    ├── screenshot 2.png
    ├── screenshot 3.png
    ├── screenshot 4.png
    ├── screenshot 5.png
    └── scrrenshot 6.png
```

---

## Parameters (inputs)

The app and scaler expect these **8 features** (same column order as in `diabetes.csv` without `Outcome`):

| Feature | Description |
|--------|--------------|
| Pregnancies | Number of pregnancies |
| Glucose | Glucose concentration (mg/dL) |
| BloodPressure | Diastolic blood pressure (mm Hg) |
| SkinThickness | Triceps skin fold thickness (mm) |
| Insulin | 2-hour serum insulin (mu U/ml) |
| BMI | Body mass index |
| DiabetesPedigreeFunction | Diabetes pedigree function |
| Age | Age (years) |

---

## Preprocess and train

`train.py` does the following:

- Loads `data/diabetes.csv`.
- Treats **0** as missing for: Glucose, BloodPressure, SkinThickness, Insulin, BMI — replaces with NaN, then fills with the **median** per column.
- **Train/test split**: 80% / 20%, stratified, `random_state=42`.
- **Scaling**: `StandardScaler` fit on the training set; same scaler used for test and saved for the app.
- **Main model**: `RandomForestClassifier` with `n_estimators=100`, `max_depth=6`, `random_state=42`.
- **Benchmark**: fits Decision Tree, Logistic Regression, KNN, Bagging, AdaBoost, Gradient Boosting, and the trained Random Forest; prints accuracy for each.
- **Saves**: `model/random_forest.pkl`, `model/scaler.pkl`.

---

## Benchmark and demo

- **Benchmark**: printed in the terminal when you run `train.py`. The Streamlit app also shows an **Architectural Benchmark Matrix** table comparing the same model family accuracies.
- **Demo**: `streamlit run app.py` — enter the eight parameters, click **Execute Diagnostic Process**, and read the risk callout and probability. The app loads `model/random_forest.pkl` and `model/scaler.pkl` from the `model/` folder (run `train.py` first if they are missing).

---

## Screenshots

### Screenshot 1

![Screenshot 1](Screenshots/screenshot%201.png)

### Screenshot 2

![Screenshot 2](Screenshots/screenshot%202.png)

### Screenshot 3

![Screenshot 3](Screenshots/screenshot%203.png)

### Screenshot 4

![Screenshot 4](Screenshots/screenshot%204.png)

### Screenshot 5

![Screenshot 5](Screenshots/screenshot%205.png)

### Screenshot 6

![Screenshot 6](Screenshots/scrrenshot%206.png)
