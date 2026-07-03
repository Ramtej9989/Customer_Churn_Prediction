# Customer Churn Prediction Using Machine Learning

## Project Overview

Customer churn is a major challenge for businesses, especially in the telecommunications industry. Identifying customers who are likely to leave a service can help companies take proactive retention measures.

This project develops an end-to-end machine learning pipeline to predict customer churn based on customer demographics, service usage, and account-related information.

Multiple classification algorithms were trained and evaluated. The Gradient Boosting Classifier achieved the best overall performance and was selected as the final machine learning model.

---

## Problem Statement

The objective of this project is to develop a machine learning model capable of predicting whether a customer is likely to churn.

By identifying customers at risk of leaving, businesses can develop targeted retention strategies and improve customer satisfaction.

---

## Project Workflow

The project follows a structured end-to-end machine learning workflow:

1. Data Understanding
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Data Preprocessing
6. Model Building
7. Model Evaluation
8. Hyperparameter Tuning
9. Model Saving
10. Project Documentation

---

## Project Structure

```text
Customer-Churn-Prediction/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   ├── customer_churn_model.pkl
│   └── feature_names.pkl
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_exploratory_data_analysis.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_data_preprocessing.ipynb
│   └── 06_model_building.ipynb
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Jupyter Notebook
- Git
- GitHub

---

## Data Understanding

The dataset was initially explored to understand its structure, features, data types, missing values, and target variable.

The analysis focused on understanding customer demographic information, service usage, account information, and customer churn behavior.

---

## Data Cleaning

Data cleaning was performed to improve data quality and prepare the dataset for analysis.

The following tasks were carried out:

- Checked missing values
- Identified duplicate records
- Corrected data types
- Handled inconsistent values
- Prepared a cleaned dataset for further analysis

---

## Exploratory Data Analysis

Exploratory Data Analysis was performed to understand customer behavior and identify patterns related to customer churn.

The analysis included:

- Customer churn distribution
- Customer demographic analysis
- Service usage patterns
- Customer tenure analysis
- Contract type analysis
- Monthly charges analysis
- Feature relationships and correlations

Visualizations were created using Matplotlib and Seaborn.

---

## Feature Engineering

Feature engineering was performed to prepare meaningful input variables for machine learning.

Categorical features were transformed into numerical representations and relevant features were prepared for model training.

---

## Data Preprocessing

The dataset was prepared for machine learning through:

- Feature and target separation
- Categorical feature encoding
- Train-test splitting
- Feature scaling where required
- Preparation of training and testing datasets

---

## Machine Learning Models

Multiple classification algorithms were trained and evaluated:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- K-Nearest Neighbors
- Naive Bayes
- Support Vector Machine
- Gradient Boosting Classifier

The performance of the models was compared using multiple classification evaluation metrics.

---

## Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score
- Confusion Matrix
- Classification Report

After comparing the trained models, the Gradient Boosting Classifier was selected as the best-performing model.

### Model Performance

| Metric | Score |
| --- | --- |
| Accuracy | 76.45% |
| Precision | 78.56% |
| Recall | 76.71% |
| F1 Score | 77.62% |
| ROC-AUC Score | 83.78% |

The model demonstrated balanced precision and recall and achieved a ROC-AUC score of approximately 83.78%, indicating good ability to distinguish between churn and non-churn customers.

---

## Hyperparameter Tuning

Hyperparameter tuning was performed on the Gradient Boosting Classifier to optimize model performance.

GridSearchCV was used to evaluate different combinations of model hyperparameters using cross-validation.

The best estimator identified during hyperparameter tuning was selected as the optimized model.

---

## Model Saving

The final trained model was saved using Joblib for future inference and deployment.

The following model artifacts were created:

- `customer_churn_model.pkl` - Saved machine learning model
- `feature_names.pkl` - Saved input feature names and feature order

Saving the trained model eliminates the need to retrain the model whenever predictions are required.

---

## Installation and Setup

Clone the repository:

```bash
git clone : "github.com/Ramtej9989/Customer_Churn_Prediction"
```

Navigate to the project directory:

```bash
cd Customer-Churn-Prediction
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on macOS or Linux:

```bash
source .venv/bin/activate
```

For Windows:

```bash
.venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open the notebooks in numerical order to explore the complete machine learning workflow.

---

## Future Improvements

The project can be further improved by:

- Handling class imbalance using advanced techniques
- Performing additional feature engineering
- Optimizing the classification probability threshold
- Using SHAP for model explainability
- Building a Flask or FastAPI prediction API
- Developing an interactive prediction interface
- Deploying the model to a cloud platform
- Implementing model monitoring and retraining

---

## Conclusion

This project demonstrates a complete end-to-end machine learning workflow for customer churn prediction.

The project covers data understanding, data cleaning, exploratory data analysis, feature engineering, preprocessing, machine learning model development, model evaluation, hyperparameter tuning, and model persistence.

Multiple classification algorithms were evaluated, and the Gradient Boosting Classifier was selected based on its overall performance.

The project demonstrates practical skills in Python, data analysis, machine learning, model evaluation, and end-to-end data science project development.

---

## Author

**Rama Satya Teja Bonthu**

AI & Data Science Graduate