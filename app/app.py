from pathlib import Path
import sys

from flask import Flask, render_template, request


# --------------------------------------------------
# Project Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

SRC_PATH = BASE_DIR / "src"

sys.path.append(str(SRC_PATH))


# --------------------------------------------------
# Import Prediction Function
# --------------------------------------------------

from predict import predict_churn


# --------------------------------------------------
# Create Flask Application
# --------------------------------------------------

app = Flask(__name__)


# --------------------------------------------------
# Home Route
# --------------------------------------------------

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        try:

            # ------------------------------------------
            # Get Customer Data From Form
            # ------------------------------------------

            customer_data = {

                "Gender": request.form.get("Gender"),

                "Age": int(
                    request.form.get("Age")
                ),

                "SeniorCitizen": int(
                    request.form.get("SeniorCitizen")
                ),

                "Partner": request.form.get("Partner"),

                "Dependents": request.form.get("Dependents"),

                "TenureMonths": int(
                    request.form.get("TenureMonths")
                ),

                "PhoneService": request.form.get(
                    "PhoneService"
                ),

                "InternetService": request.form.get(
                    "InternetService"
                ),

                "OnlineSecurity": request.form.get(
                    "OnlineSecurity"
                ),

                "OnlineBackup": request.form.get(
                    "OnlineBackup"
                ),

                "DeviceProtection": request.form.get(
                    "DeviceProtection"
                ),

                "TechSupport": request.form.get(
                    "TechSupport"
                ),

                "StreamingTV": request.form.get(
                    "StreamingTV"
                ),

                "StreamingMovies": request.form.get(
                    "StreamingMovies"
                ),

                "Contract": request.form.get("Contract"),

                "PaymentMethod": request.form.get(
                    "PaymentMethod"
                ),

                "MonthlyCharges": float(
                    request.form.get("MonthlyCharges")
                ),

                "TotalCharges": float(
                    request.form.get("TotalCharges")
                ),

                "SupportTickets": int(
                    request.form.get("SupportTickets")
                ),

                "SatisfactionScore": int(
                    request.form.get("SatisfactionScore")
                ),

                "AverageMonthlySpend": float(
                    request.form.get(
                        "AverageMonthlySpend"
                    )
                )
            }


            # ------------------------------------------
            # Predict Customer Churn
            # ------------------------------------------

            result = predict_churn(customer_data)


        except Exception as error:

            result = {

                "prediction": "ERROR",

                "churn_probability": 0,

                "risk_level": str(error)
            }


    # --------------------------------------------------
    # Render Web Page
    # --------------------------------------------------

    return render_template(
        "index.html",
        result=result
    )


# --------------------------------------------------
# Run Flask Application
# --------------------------------------------------

if __name__ == "__main__":

    app.run(
        debug=True
    )