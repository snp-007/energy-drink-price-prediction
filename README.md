# Beverage Price Range Prediction
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?logo=numpy)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?logo=scikitlearn)
![LightGBM](https://img.shields.io/badge/LightGBM-Best%20Model-02569B)
![XGBoost](https://img.shields.io/badge/XGBoost-Gradient%20Boosting-EC6B23)
![MLflow](https://img.shields.io/badge/MLflow-Experiment%20Tracking-0194E2)
![DagsHub](https://img.shields.io/badge/DagsHub-MLOps-6E56CF)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed%20App-FF4B4B?logo=streamlit)
![Accuracy](https://img.shields.io/badge/Accuracy-92.51%25-success)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)
![Live Demo](https://img.shields.io/badge/Live-Demo-success?logo=streamlit)
![Last Commit](https://img.shields.io/github/last-commit/snp-007/energy-drink-price-prediction)
![Repo Size](https://img.shields.io/github/repo-size/snp-007/energy-drink-price-prediction)
![Stars](https://img.shields.io/github/stars/snp-007/energy-drink-price-prediction?style=social)
![License](https://img.shields.io/badge/License-Educational-lightgrey)
## End-to-End Machine Learning, MLOps & Streamlit Deployment Project



# 📌 Project Overview

This project predicts a consumer's preferred energy drink price range using demographic, behavioral, and engineered survey features.

The solution follows a complete industry-standard Machine Learning workflow:

* Data Cleaning
* Feature Engineering
* Data Preprocessing
* Model Development
* Model Comparison
* MLFlow Experiment Tracking
* DagsHub Model Versioning
* Streamlit Deployment

The final production model achieved **92.51% accuracy** using **LightGBM**.

---

# 🎯 Business Problem

A Beverage company wants to better understand customer purchasing behavior and pricing preferences.

The objective is to predict the preferred energy drink price range of consumers based on:

* Demographics
* Consumption behavior
* Brand preferences
* Health awareness
* Purchase patterns

This enables:

* Better pricing strategies
* Customer segmentation
* Targeted marketing campaigns
* Product positioning

---

# 📊 Dataset Overview

The dataset contains consumer survey responses.

### Features

* Age
* Gender
* Zone
* Occupation
* Income Levels
* Consumption Frequency
* Current Brand
* Brand Awareness
* Purchase Channel
* Packaging Preference
* Health Concerns
* Consumption Situations
* Flavor Preference

### Target Variable

```text
price_range
```

Classes:

* 50-100
* 100-150
* 150-200
* 200-250

---

# 🧹 Data Cleaning

Performed:

* Missing value treatment
* Duplicate removal
* Typographical corrections
* Age outlier handling
* Logical outlier removal
* Category standardization

### Examples

Corrected:

```text
Metor → Metro
urbna → Urban
Establishd → Established
newcomer → Newcomer
```

---

# ⚙️ Feature Engineering

Created the following features:

| Feature     | Description                             |
| ----------- | --------------------------------------- |
| age_group   | Categorized age brackets                |
| cf_ab_score | Consumption Frequency & Awareness Score |
| zas_score   | Zone Affluence Score                    |
| bsi         | Brand Switching Indicator               |

These engineered features significantly improved model performance.

---

# 🔄 Data Preprocessing

Performed:

* Train-Test Split (75:25)
* Label Encoding
* One-Hot Encoding
* Feature Scaling (for applicable models)

Final Dataset:

```text
Rows: 29,965
Features: 27
```

---

# 🤖 Machine Learning Models

The following models were trained and evaluated:

1. Gaussian Naive Bayes
2. Logistic Regression
3. Support Vector Machine (SVM)
4. Random Forest
5. XGBoost
6. LightGBM

---

# 📈 Model Performance

| Model                | Accuracy   |
| -------------------- | ---------- |
| Gaussian Naive Bayes | 56.18%     |
| Logistic Regression  | 80.34%     |
| SVM                  | 86.55%     |
| Random Forest        | 89.71%     |
| XGBoost              | 92.11%     |
| LightGBM             | **92.51%** |

---

# 🏆 Best Model

## LightGBM

### Accuracy

```text
92.51%
```

LightGBM delivered the best overall performance and was selected as the production model.

---

# 📊 Feature Importance Insights

Top predictors identified by LightGBM:

1. consume_frequency(weekly)
2. health_concerns
3. zas_score
4. age_group
5. income_levels
6. cf_ab_score
7. bsi

### Business Insight

Consumer spending behavior is strongly influenced by:

* Consumption frequency
* Socioeconomic status
* Health awareness
* Brand loyalty

---

# 🔬 MLFlow Experiment Tracking

MLFlow was integrated for experiment tracking.

Tracked:

* Parameters
* Accuracy
* Precision
* Recall
* F1 Score
* Model Artifacts

### Logged Models

* Gaussian Naive Bayes
* Logistic Regression
* SVM
* Random Forest
* XGBoost
* LightGBM

---

# 🚀 DagsHub Integration

DagsHub was used for:

* Experiment Tracking
* Artifact Storage
* Model Versioning
* Experiment Visualization

### Repository

```text
energy-drink-price-prediction
```

---

# 🌐 Streamlit Application

A production-ready Streamlit application was developed to demonstrate the solution.

### Features

* Interactive user interface
* Real-time predictions
* Confidence score display
* LightGBM-powered inference
* Professional dashboard layout
* Custom CodeX branding

### User Inputs

* Demographics
* Consumption behavior
* Brand awareness
* Purchase preferences

### Output

```text
Predicted Price Range
Confidence Score
```

---

# 🏗 Project Structure

```bash
energy-drink-price-prediction/
│
├── app/
│   ├── app.py
│   ├── utils.py
│   ├── config.py
│   │
│   ├── artifacts/
│   │   ├── lgbm_model.pkl
│   │   ├── scaler.pkl
│   │   ├── target_encoder.pkl
│   │   ├── feature_label_encoders.pkl
│   │   └── model_columns.pkl
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── data_cleaning.ipynb
│   ├── feature_engineering.ipynb
│   ├── modeling.ipynb
│   └── mlflow_tracking.ipynb
│
├── outputs/
│   ├── models/
│   ├── reports/
│   └── plots/
│
├── requirements.txt
└── README.md
```

---

# 💾 Saved Artifacts

### Models

* gnb_model.pkl
* lr_model.pkl
* svm_model.pkl
* rf_model.pkl
* xgb_model.pkl
* lgbm_model.pkl

### Supporting Objects

* scaler.pkl
* target_encoder.pkl
* feature_label_encoders.pkl
* model_columns.pkl

---

# 🛠 Technology Stack

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn
* XGBoost
* LightGBM

### MLOps

* MLFlow
* DagsHub
* Joblib

### Deployment

* Streamlit

---

# 🚀 Running the Application

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch Streamlit:

```bash
streamlit run app/app.py
```

---

# 🔮 Future Improvements

Potential enhancements:

* Hyperparameter tuning
* SHAP Explainability
* Docker Containerization
* Streamlit Cloud Deployment
* AWS Deployment
* CI/CD Pipeline Integration
* Monitoring & Drift Detection

---

# 👨‍💻 Author

**Siba Narayana Parida**

Pre-Final Year Undergraduate
National Institute of Technology Rourkela

Interests:

* Machine Learning
* Data Science
* MLOps
* Software Development

---

# 📜 License

This project is developed for educational, research, and portfolio purposes.

© 2026 Siba Narayana Parida™
