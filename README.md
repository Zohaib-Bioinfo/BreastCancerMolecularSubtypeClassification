# 🧬 Breast Cancer Molecular Subtype Classification using Transcriptomics (GSE45827)

## 📌 Project Overview
This project applies machine learning and transcriptomic analysis to classify breast cancer molecular subtypes using gene expression profiles from the NCBI GEO dataset **GSE45827**.

The goal is to identify biologically meaningful patterns in gene expression data and build an interpretable predictive model for cancer subtype classification.

---

## 🎯 Objectives
- Analyze high-dimensional gene expression data
- Perform preprocessing and normalization
- Select informative genes (biomarkers)
- Train machine learning models for classification
- Evaluate performance using statistical metrics
- Develop an interpretable biomedical AI system

---

## 🧬 Dataset Information
- **Source:** NCBI Gene Expression Omnibus (GEO)
- **Dataset ID:** GSE45827
- **Type:** Transcriptomic gene expression data
- **Classes:**
  - Breast cancer subtypes
  - Normal tissue samples

---

## ⚙️ Methodology

### 1. Data Preprocessing
- Missing value handling
- Log transformation (if applicable)
- Standard scaling of gene expression values

### 2. Feature Selection
- Statistical filtering using SelectKBest / ANOVA-F
- Dimensionality reduction for high-dimensional gene space

### 3. Model Development
- Machine Learning models trained on selected genes:
  - Random Forest / Neural Network (depending on implementation)
- Train-test split with class balancing

### 4. Evaluation Metrics
- Accuracy
- ROC-AUC Score
- Precision, Recall, F1-score
- Confusion Matrix

### 5. Explainability (Optional Extension)
- Feature importance analysis
- Biomarker gene identification

---

## 🤖 Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib / Seaborn
- Streamlit (for web interface)
- GEOparse (dataset retrieval)

---

## 📊 Results Summary
- High classification performance achieved on test data
- Identification of potential biomarker genes
- Demonstrated feasibility of ML in transcriptomics-based cancer classification

---

## 🧪 How to Run the Project

### 1. Install dependencies
```bash
pip install -r requirements.txt
