
import streamlit as st
import numpy as np
import pandas as pd
import pickle
import shap
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# LOAD MODELS
# -----------------------------
model = pickle.load(open("models/model.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))
selector = pickle.load(open("models/selector.pkl", "rb"))
genes = pickle.load(open("data/genes.pkl", "rb"))
encoder = pickle.load(open("models/encoder.pkl", "rb"))

st.set_page_config(page_title="Breast Cancer Transcriptomics", layout="wide")

# -----------------------------
# TITLE
# -----------------------------
st.title("🧬 Breast Cancer Transcriptomics Classifier")
st.markdown("### GSE45827 | ML + SHAP + Biomarker Analysis")

# -----------------------------
# SIDEBAR NAVIGATION
# -----------------------------
page = st.sidebar.selectbox(
    "Navigation",
    ["Dataset Overview", "Gene Explorer", "Prediction Tool", "Biomarkers + SHAP"]
)

# -----------------------------
# PAGE 1: DATASET OVERVIEW
# -----------------------------
if page == "Dataset Overview":

    st.header("📊 Dataset Overview (GSE45827)")

    st.markdown("""
    - Breast cancer gene expression dataset  
    - Subtypes: TNBC, HER2, Luminal A, Luminal B, Normal  
    - Platform: Microarray (Affymetrix)  
    """)

    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3b/DNA_double_helix_vertical.png")

    st.info("This project uses transcriptomic gene expression data for cancer subtype classification.")

# -----------------------------
# PAGE 2: GENE EXPLORER
# -----------------------------
elif page == "Gene Explorer":

    st.header("🔬 Gene Expression Explorer")

    gene = st.selectbox("Select Gene", genes)

    st.write(f"Showing simulated expression pattern for: {gene}")

    # fake visualization (replace with real dataset in final version)
    data = pd.DataFrame({
        "Subtype": ["Normal", "TNBC", "HER2", "LuminalA", "LuminalB"],
        "Expression": np.random.rand(5) * 10
    })

    fig, ax = plt.subplots()
    sns.barplot(data=data, x="Subtype", y="Expression", ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# -----------------------------
# PAGE 3: PREDICTION TOOL
# -----------------------------
elif page == "Prediction Tool":

    st.header("🤖 Breast Cancer Subtype Prediction")

    st.write("Enter gene expression values:")

    input_data = []

    for i in range(10):  # demo input (you will expand later)
        val = st.number_input(f"Gene {i+1}", value=0.0)
        input_data.append(val)

    if st.button("Predict Subtype"):

        X = np.array(input_data).reshape(1, -1)

        X = scaler.transform(X)
        X = selector.transform(X)

        pred = model.predict(X)
        prob = model.predict_proba(X)

        label = encoder.inverse_transform(pred)[0]

        st.success(f"Predicted Subtype: {label}")

        st.write("Probability:")
        st.write(prob)

# -----------------------------
# PAGE 4: BIOMARKERS + SHAP
# -----------------------------
elif page == "Biomarkers + SHAP":

    st.header("🧬 Biomarker Genes & Explainability")

    st.subheader("Top Biomarker Genes")

    # placeholder (replace with real top_genes.csv)
    top_genes = pd.DataFrame({
        "Gene": genes[:10],
        "Importance": np.random.rand(10)
    })

    st.dataframe(top_genes)

    fig, ax = plt.subplots()
    sns.barplot(data=top_genes, x="Importance", y="Gene", ax=ax)
    st.pyplot(fig)

    st.subheader("SHAP Explanation")

    st.info("SHAP visualization requires model inference data.")

    # dummy SHAP plot placeholder
    fig, ax = plt.subplots()
    ax.barh(["Gene1", "Gene2", "Gene3"], [0.2, 0.5, 0.3])
    st.pyplot(fig)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.markdown("Developed for Bioinformatics Research Project | GSE45827")
