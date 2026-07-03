import joblib
import pandas as pd

from pathlib import Path
from preprocess_input import preprocess_customer_input


# --------------------------------------------------
# Project Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = (
    BASE_DIR
    / "models"
    / "customer_churn_model.pkl"
)

FEATURE_NAMES_PATH = (
    BASE_DIR
    / "models"
    / "feature_names.pkl"
)


# --------------------------------------------------
# Load Model
# --------------------------------------------------

model = joblib.load(MODEL_PATH)

feature_names = joblib.load(
    FEATURE_NAMES_PATH
)

print(
    "Customer Churn Prediction System "
    "loaded successfully!"
)


# --------------------------------------------------
# Prediction Function
# --------------------------------------------------

def predict_churn(customer_data):
    """
    Predict customer churn using normal customer data.

    Returns:
        Prediction
        Churn probability
        Risk level
    """

    # Convert normal customer data
    # into model features

    processed_data = preprocess_customer_input(
        customer_data
    )

    # Convert to DataFrame

    customer_df = pd.DataFrame(
        [processed_data]
    )

    # Ensure exact feature order

    customer_df = customer_df.reindex(
        columns=feature_names,
        fill_value=0
    )

    # Make prediction

    prediction = model.predict(
        customer_df
    )[0]

    # Calculate churn probability

    churn_probability = model.predict_proba(
        customer_df
    )[0][1]

    # Determine risk level

    if churn_probability < 0.30:

        risk_level = "LOW RISK"

    elif churn_probability < 0.70:

        risk_level = "MEDIUM RISK"

    else:

        risk_level = "HIGH RISK"

    # Return prediction result

    return {

        "prediction": (
            "CHURN"
            if prediction == 1
            else "NOT CHURN"
        ),

        "churn_probability": round(
            churn_probability * 100,
            2
        ),

        "risk_level": risk_level
    }


# --------------------------------------------------
# Test Prediction
# --------------------------------------------------

if __name__ == "__main__":

    customer_data = {

        "Gender": "Male",

        "Age": 25,

        "SeniorCitizen": 0,

        "Partner": "No",

        "Dependents": "No",

        "TenureMonths": 5,

        "PhoneService": "Yes",

        "InternetService": "Fiber Optic",

        "OnlineSecurity": "No",

        "OnlineBackup": "No",

        "DeviceProtection": "No",

        "TechSupport": "No",

        "StreamingTV": "Yes",

        "StreamingMovies": "Yes",

        "Contract": "Month-to-month",

        "PaymentMethod": "Electronic Check",

        "MonthlyCharges": 95,

        "TotalCharges": 475,

        "SupportTickets": 7,

        "SatisfactionScore": 1,

        "AverageMonthlySpend": 95
    }


    result = predict_churn(
        customer_data
    )


    print(
        "\nCustomer Churn Prediction"
    )

    print(
        "-------------------------"
    )

    print(
        "Prediction:",
        result["prediction"]
    )

    print(
        "Churn Probability:",
        f'{result["churn_probability"]}%'
    )

    print(
        "Risk Level:",
        result["risk_level"]
    )