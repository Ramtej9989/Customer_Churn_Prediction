# Customer Churn Prediction Using Machine Learning

## Project Overview

Customer churn is a major challenge for businesses, especially in the telecommunications industry. Identifying customers who are likely to leave a service can help companies take proactive retention measures and improve customer retention.

This project develops an end-to-end machine learning pipeline to predict customer churn based on customer demographics, service usage, and account-related information.

Multiple classification algorithms were trained and evaluated. The **Gradient Boosting Classifier** achieved the best overall performance and was selected as the final machine learning model.

---

## Problem Statement

The objective of this project is to develop a machine learning model capable of predicting whether a customer is likely to churn.

By identifying customers at risk of leaving, businesses can develop targeted retention strategies, improve customer satisfaction, and reduce customer loss.

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
Customer_Churn_Prediction/
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

The analysis focused on customer demographic information, service usage, account-related information, and customer churn behavior.

Key data understanding tasks included:

- Examining dataset dimensions
- Understanding feature data types
- Identifying missing values
- Checking duplicate records
- Analyzing the target variable
- Reviewing categorical and numerical features

---

## Data Cleaning

Data cleaning was performed to improve data quality and prepare the dataset for further analysis.

The following tasks were carried out:

- Checked missing values
- Identified duplicate records
- Corrected data types
- Handled inconsistent values
- Prepared a cleaned dataset for exploratory data analysis and machine learning

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

Visualizations were created using **Matplotlib** and **Seaborn** to identify trends and patterns within the dataset.

---

## Feature Engineering

Feature engineering was performed to prepare meaningful input variables for machine learning.

The process included:

- Transforming categorical features
- Preparing numerical representations of categorical variables
- Selecting relevant input features
- Preparing the target variable
- Ensuring features were suitable for machine learning algorithms

---

## Data Preprocessing

The dataset was prepared for machine learning through the following preprocessing steps:

- Feature and target separation
- Categorical feature encoding
- Train-test splitting
- Feature scaling where required
- Preparation of training and testing datasets

These preprocessing steps ensured that the dataset was suitable for training multiple machine learning models.

---

## Machine Learning Models

Multiple classification algorithms were trained and evaluated to identify the most suitable model for customer churn prediction.

The following machine learning models were used:

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

The machine learning models were evaluated using the following metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score
- Confusion Matrix
- Classification Report

After comparing the trained models, the **Gradient Boosting Classifier** was selected as the best-performing model based on its overall performance.

### Model Performance

| Metric | Score |
| --- | --- |
| Accuracy | 76.45% |
| Precision | 78.56% |
| Recall | 76.71% |
| F1 Score | 77.62% |
| ROC-AUC Score | 83.78% |

The Gradient Boosting model demonstrated a good balance between precision and recall.

The ROC-AUC score of approximately **83.78%** indicates that the model has a strong ability to distinguish between customers who are likely to churn and customers who are likely to remain.

---

## Hyperparameter Tuning

Hyperparameter tuning was performed on the **Gradient Boosting Classifier** to optimize model performance.

**GridSearchCV** was used to systematically evaluate different combinations of model hyperparameters using cross-validation.

The tuning process focused on identifying an optimal combination of model parameters.

The best estimator identified during the GridSearchCV process was selected as the optimized machine learning model.

---

## Model Saving

The final trained machine learning model was saved using **Joblib** for future inference and deployment.

The following model artifacts were created:

- `customer_churn_model.pkl` - Final trained machine learning model
- `feature_names.pkl` - Input feature names and feature order

Saving the trained model eliminates the need to retrain the machine learning model whenever predictions are required.

The saved model can be integrated into a web application, API, or other prediction system in the future.

---

## Installation and Setup

Clone the repository:

```bash
git clone https://github.com/Ramtej9989/Customer_Churn_Prediction.git
```

Navigate to the project directory:

```bash
cd Customer_Churn_Prediction
```

Create a virtual environment:

```bash
python -m venv .venv
```

### Activate the Virtual Environment

For macOS or Linux:

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

## Notebook Execution Order

Run the notebooks in the following order:

```text
01_data_understanding.ipynb
        ↓
02_data_cleaning.ipynb
        ↓
03_exploratory_data_analysis.ipynb
        ↓
04_feature_engineering.ipynb
        ↓
05_data_preprocessing.ipynb
        ↓
06_model_building.ipynb
```

Each notebook represents a specific stage of the machine learning workflow.

---

## Key Project Outcomes

- Developed an end-to-end customer churn prediction machine learning pipeline
- Performed data cleaning and exploratory data analysis
- Analyzed customer behavior and churn patterns
- Performed feature engineering and data preprocessing
- Trained multiple classification algorithms
- Compared models using multiple evaluation metrics
- Selected Gradient Boosting as the best-performing classifier
- Applied hyperparameter tuning using GridSearchCV
- Saved the final trained model using Joblib
- Organized the project using a professional data science project structure

---

## Future Improvements

The project can be further improved by:

- Handling class imbalance using advanced resampling techniques
- Performing additional feature engineering
- Optimizing the classification probability threshold
- Using SHAP for model explainability
- Developing a Flask or FastAPI prediction API
- Building an interactive customer churn prediction interface
- Deploying the model to a cloud platform
- Implementing model monitoring and automated retraining

---

## Conclusion

This project demonstrates a complete end-to-end machine learning workflow for customer churn prediction.

The project covers data understanding, data cleaning, exploratory data analysis, feature engineering, preprocessing, machine learning model development, model evaluation, hyperparameter tuning, and model persistence.

Multiple classification algorithms were trained and evaluated. The **Gradient Boosting Classifier** was selected based on its overall performance.

The final model achieved an **Accuracy of 76.45%** and a **ROC-AUC score of 83.78%**, demonstrating good predictive and class discrimination performance.

This project demonstrates practical skills in **Python, Data Analysis, Exploratory Data Analysis, Machine Learning, Model Evaluation, Hyperparameter Tuning, and end-to-end Data Science project development**.

---

## Author

**Rama Satya Teja Bonthu**

AI & Data Science Graduate

GitHub: Ramtej9989