# ============================================================
#         ENSEMBLE LEARNING - DIABETES PREDICTION
#         app.py — Model Context Protocol Docs Theme (Fixed)
# ============================================================

import streamlit as st
import numpy as np
import joblib
import pandas as pd

# ── Page Config ───────────────────────────────────────────────
st.set_page_config(
    page_title="Diabetes Health Analytics",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Load Model & Scaler ───────────────────────────────────────
model  = joblib.load("model/random_forest.pkl")
scaler = joblib.load("model/scaler.pkl")

# ── Official MCP Docs Pure Light Theme CSS ────────────────────
st.markdown("""
<style>
/* ── Force Global Light Background & Reset ── */
html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
    background-color: #ffffff !important;
    color: #1f2937 !important;
}

/* ── Absolute Destruction of Ghost Boxes & Border Outlines ── */
div[data-testid="stGridHorizontal"] > div,
div[data-testid="stHorizontalBlock"] > div,
div[data-testid="stVerticalBlock"] > div {
    background-color: transparent !important;
}

/* Hard target and remove empty layout column wrappers causing the ghost boxes */
div[data-testid="column"] {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

/* Nuke native empty column placeholders */
div[data-testid="elementContainer"]:empty, 
div.element-container:empty,
div[data-testid="stVerticalBlock"] > div:empty {
    display: none !important;
    height: 0px !important;
    padding: 0px !important;
    margin: 0px !important;
}

/* ── Main Layout Workspace ── */
.main .block-container {
    background-color: #ffffff !important;
    padding: 3rem 5rem !important;
    max-width: 1300px;
}

/* ── MCP Docs Header Layout ── */
.mcp-header {
    border-bottom: 1px solid #e5e7eb;
    padding-bottom: 24px;
    margin-bottom: 36px;
}
.mcp-title {
    font-size: 30px;
    font-weight: 700;
    color: #111827;
    letter-spacing: -0.025em;
}
.mcp-subtitle {
    font-size: 15px;
    color: #4b5563;
    margin-top: 6px;
}

/* ── MCP Clean Document Cards ── */
.mcp-card {
    background: #ffffff !important;
    border: 1px solid #e5e7eb !important;
    border-radius: 8px;
    padding: 26px;
    margin-bottom: 24px;
    box-shadow: none !important;
}

.mcp-section-title {
    font-size: 15px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #4b5563;
    margin-bottom: 24px;
    display: flex;
    align-items: center;
    gap: 8px;
}

/* ── Hard Override for Number Input Wrapper Blocks ── */
div[data-testid="stNumberInput"] {
    background-color: transparent !important;
}

/* ── Complete Input Field Text/Fill Overrides ── */
div[data-baseweb="input"], [data-baseweb="input"] > div {
    background-color: #f9fafb !important;
    border: 1px solid #d1d5db !important;
    border-radius: 6px !important;
}

input[type="number"] {
    color: #111827 !important;
    background-color: #f9fafb !important;
    font-weight: 500 !important;
}

label p {
    color: #374151 !important;
    font-weight: 500 !important;
    font-size: 14px !important;
}

/* Plus and minus step button targets - Forced Light Mode */
div[data-baseweb="input"] button, 
div[data-testid="stNumberInput"] button {
    background-color: #f3f4f6 !important;
    color: #374151 !important;
    border: 1px solid #d1d5db !important;
    border-radius: 4px !important;
}
div[data-baseweb="input"] button:hover,
div[data-testid="stNumberInput"] button:hover {
    background-color: #e5e7eb !important;
}

/* ── Core Metric Boxes ── */
.mcp-metric-row {
    display: flex;
    gap: 16px;
    margin-bottom: 20px;
}
.mcp-metric-card {
    flex: 1;
    background: #f9fafb;
    border: 1px solid #e5e7eb;
    border-radius: 6px;
    padding: 14px;
    text-align: center;
}
.mcp-metric-val {
    font-size: 24px;
    font-weight: 700;
    color: #111827;
}
.mcp-metric-lbl {
    font-size: 12px;
    color: #6b7280;
    margin-top: 2px;
}

/* ── Premium MCP Status Callouts ── */
.mcp-callout {
    border-radius: 6px;
    padding: 20px;
    margin-top: 12px;
    font-size: 14px;
    line-height: 1.5;
}
.mcp-callout-positive {
    background-color: #fef2f2 !important;
    border: 1px solid #fca5a5 !important;
    color: #991b1b !important;
}
.mcp-callout-negative {
    background-color: #f0fdf4 !important;
    border: 1px solid #86efac !important;
    color: #166534 !important;
}
.mcp-callout-title {
    font-weight: 700;
    font-size: 15px;
    margin-bottom: 6px;
}

/* ── MCP Doc Indigo Accent Button ── */
div.stButton > button {
    background-color: #4f46e5 !important;
    color: #ffffff !important;
    border: 1px solid #4338ca !important;
    border-radius: 6px !important;
    padding: 10px 24px !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    width: auto !important;
    min-width: 200px;
    transition: all 0.15s ease;
    box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
}
div.stButton > button:hover {
    background-color: #4338ca !important;
    border-color: #3730a3 !important;
}

/* ── Premium Light Theme Benchmarking Dataframe Overrides ── */
div[data-testid="stDataFrame"], div[data-testid="stDataFrame"] > div {
    background-color: #ffffff !important;
    border: 1px solid #e5e7eb !important;
    border-radius: 6px !important;
}

/* Force Light Background for Table Cells and Headers */
div[data-testid="stDataFrame"] [role="columnheader"], 
div[data-testid="stDataFrame"] [role="gridcell"],
div[data-testid="stDataFrame"] data-grid-canvas,
div[data-testid="stDataFrame"] [class*="glideDataGrid"] {
    background-color: #ffffff !important;
    color: #1f2937 !important;
}

/* Specific styling target for Table Headings background color */
div[data-testid="stDataFrame"] [role="columnheader"] {
    background-color: #f9fafb !important;
    color: #374151 !important;
    font-weight: 600 !important;
}

/* Text visibility inside any embedded elements */
div[data-testid="stDataFrame"] * {
    color: #1f2937 !important;
    font-family: inherit !important;
}
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────
st.markdown("""
<div class="mcp-header">
    <div class="mcp-title">Diabetes Health Analytics</div>
    <div class="mcp-subtitle">An open architecture decision helper powered by Random Forest Ensemble Learning.</div>
</div>
""", unsafe_allow_html=True)

# ── Workspace Columns Layout ──────────────────────────────────
col_left, col_right = st.columns([1.3, 1])

# ── Left Column: Inputs ───────────────────────────────────────
with col_left:
    st.markdown('<div class="mcp-card">', unsafe_allow_html=True)
    st.markdown('<div class="mcp-section-title">📋 Patient Features Definition</div>', unsafe_allow_html=True)
    
    sub_col1, sub_col2 = st.columns(2)
    with sub_col1:
        pregnancies = st.number_input("Pregnancies", min_value=0, max_value=17, value=3, step=1)
        glucose     = st.number_input("Glucose Concentration (mg/dL)", min_value=0, max_value=200, value=120, step=1)
        blood_press = st.number_input("Blood Pressure (mm Hg)", min_value=0, max_value=122, value=70, step=1)
        skin_thick  = st.number_input("Skin Triceps Thickness (mm)", min_value=0, max_value=99, value=20, step=1)
        
    with sub_col2:
        insulin     = st.number_input("Serum Insulin (mu U/ml)", min_value=0, max_value=846, value=79, step=1)
        bmi         = st.number_input("Body Mass Index (BMI)", min_value=0.0, max_value=67.1, value=32.0, step=0.1)
        dpf         = st.number_input("Diabetes Pedigree Function", min_value=0.07, max_value=2.42, value=0.47, step=0.01)
        age         = st.number_input("Patient Age (Years)", min_value=21, max_value=81, value=33, step=1)
        
    predict_btn = st.button("Execute Diagnostic Process")
    st.markdown('</div>', unsafe_allow_html=True)

# ── Right Column: Diagnostic Output ───────────────────────────
with col_right:
    st.markdown('<div class="mcp-card" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown('<div class="mcp-section-title">🎯 Assessment Report</div>', unsafe_allow_html=True)
    
    if predict_btn:
        # Columns precisely named to map straight to synchronized scaler pipelines
        features_df = pd.DataFrame([{
            "Pregnancies"             : float(pregnancies),
            "Glucose"                 : float(glucose),
            "BloodPressure"           : float(blood_press),
            "SkinThickness"           : float(skin_thick),
            "Insulin"                 : float(insulin),
            "BMI"                     : float(bmi),
            "DiabetesPedigreeFunction": float(dpf),
            "Age"                     : float(age)
        }])
        
        input_scaled = scaler.transform(features_df)
        prediction  = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0][1] * 100
        
        st.markdown(f"""
        <div class="mcp-metric-row">
            <div class="mcp-metric-card">
                <div class="mcp-metric-val">{glucose}</div>
                <div class="mcp-metric-lbl">Glucose Level</div>
            </div>
            <div class="mcp-metric-card">
                <div class="mcp-metric-val">{bmi:.1f}</div>
                <div class="mcp-metric-lbl">BMI Value</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if prediction == 1:
            st.markdown(f"""
            <div class="mcp-callout mcp-callout-positive">
                <div class="mcp-callout-title">⚠️ High Risk / Positive Outcome</div>
                The ensemble classifier detected abnormal variations. Profile calculation implies a <strong>{probability:.1f}%</strong> risk vector.
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="mcp-callout mcp-callout-negative">
                <div class="mcp-callout-title">✅ Low Risk / Negative Outcome</div>
                Patient parameters fall into optimal historical thresholds. Calculated probability score is <strong>{probability:.1f}%</strong>.
            </div>
            """, unsafe_allow_html=True)
            
    else:
        st.markdown("""
        <div style="background-color: #f9fafb; border: 1px solid #e5e7eb; border-radius: 6px; padding: 16px; color: #4b5563; font-size: 14px;">
            ℹ️ Populate feature variables in the input matrix parameters panel and trigger code compilation execution to review outputs.
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)

# ── Benchmark Matrix Table ────────────────────────────────────
st.markdown('<div class="mcp-card">', unsafe_allow_html=True)
st.markdown('<div class="mcp-section-title">📊 Architectural Benchmark Matrix</div>', unsafe_allow_html=True)

compare_df = pd.DataFrame({
    "Framework Infrastructure Core": [
        "Decision Tree Architecture", "Logistic Regression Baseline", "K-Nearest Neighbors Instance",
        "Ensemble Meta-Estimator (Bagging)", "Adaptive Boosting Framework (AdaBoost)",
        "Gradient Optimization Engine", "Random Forest Classifier Core ⭐"
    ],
    "Accuracy Protocol Metric": ["68.18%", "70.78%", "75.32%", "74.68%", "74.68%", "75.97%", "74.03%"],
    "System Classification Taxonomy": [
        "Single Node Primitive", "Linear Core Engine", "Spatial Node Network",
        "Bootstrap Convergence Layer", "Sequential Boost Layer",
        "Loss-Minimized Tree Engine", "Distributed Subspace Ensemble"
    ]
})

st.dataframe(compare_df, use_container_width=True, hide_index=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; color:#9ca3af; font-size:12px; margin-top: 40px; padding-bottom: 20px;">
    Dataset Index: Pima Indians Diabetes Collection · Architecture Protocol: Scikit-Learn Engine Pipeline · Target Workspace: Streamlit Docs Frontend
</div>
""", unsafe_allow_html=True)