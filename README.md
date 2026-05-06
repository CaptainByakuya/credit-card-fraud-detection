
# 💳 Credit Card Fraud Detection System

## Overview

Credit card fraud is a growing problem that costs billions of dollars every year. 

This project builds a machine learning system that detects fraudulent transactions 

in real time using a dataset of 284,807 transactions.

## The Problem

Only 0.17% of transactions in the dataset are fraudulent — making this a highly 

imbalanced classification problem. The challenge is not just building a model, 

but building one that actually catches fraud without flagging every legitimate 

transaction as suspicious.

## What I Did

- Explored and visualized the dataset to understand the class imbalance

- Used **SMOTE** to handle the imbalanced data

- Trained and compared 3 models — Logistic Regression, Random Forest and XGBoost

- Evaluated models using Precision, Recall and F1 Score

- Built and deployed an interactive web app using Streamlit

## Results

| Model | Precision | Recall | F1 Score |

|-------|-----------|--------|----------|

| Logistic Regression | 0.06 | 0.92 | 0.11 |

| Random Forest | 0.94 | 0.83 | **0.88** |

| XGBoost | 0.88 | 0.80 | 0.83 |

**Random Forest** performed best with an F1 Score of 0.88 on fraud transactions.

## Live Demo

👉 https://credit-card-fraud-detection-edpfrt7myw2kkmnaqzpwdw.streamlit.app

## Technologies Used

- Python

- Pandas, NumPy

- Scikit-learn

- XGBoost

- Imbalanced-learn (SMOTE)

- Streamlit

- Joblib

## Dataset

[Kaggle Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

## How to Run Locally

```bash

git clone https://github.com/CaptainByakuya/credit-card-fraud-detection.git

cd credit-card-fraud-detection

pip install -r requirements.txt

streamlit run app.py

```

## Author

Kareem Temitope 

