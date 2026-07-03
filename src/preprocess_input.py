FEATURE_NAMES = [
    'Age',
    'SeniorCitizen',
    'TenureMonths',
    'MonthlyCharges',
    'TotalCharges',
    'SupportTickets',
    'SatisfactionScore',
    'AverageMonthlySpend',
    'Gender_Male',
    'Partner_Yes',
    'Dependents_Yes',
    'PhoneService_Yes',
    'InternetService_DSL',
    'InternetService_Fiber Optic',
    'InternetService_Unknown',
    'OnlineSecurity_No internet service',
    'OnlineSecurity_Yes',
    'OnlineBackup_No internet service',
    'OnlineBackup_Yes',
    'DeviceProtection_No internet service',
    'DeviceProtection_Yes',
    'TechSupport_No internet service',
    'TechSupport_Yes',
    'StreamingTV_No internet service',
    'StreamingTV_Yes',
    'StreamingMovies_No internet service',
    'StreamingMovies_Yes',
    'Contract_One year',
    'Contract_Two year',
    'PaymentMethod_Credit Card',
    'PaymentMethod_Electronic Check',
    'PaymentMethod_Mailed Check',
    'TenureGroup_1-2 Years',
    'TenureGroup_2-4 Years',
    'TenureGroup_4-6 Years',
    'MonthlyChargeCategory_Low',
    'MonthlyChargeCategory_Medium',
    'SupportLevel_Low',
    'SupportLevel_Medium'
]


def preprocess_customer_input(customer_data):
    """
    Convert normal customer input into the 39 features
    required by the trained machine learning model.
    """

    # Create all 39 model features with default value 0
    processed_data = {
        feature: 0 for feature in FEATURE_NAMES
    }

    # --------------------------------------------------
    # Numerical Features
    # --------------------------------------------------

    numerical_features = [
        "Age",
        "SeniorCitizen",
        "TenureMonths",
        "MonthlyCharges",
        "TotalCharges",
        "SupportTickets",
        "SatisfactionScore",
        "AverageMonthlySpend"
    ]

    for feature in numerical_features:
        processed_data[feature] = customer_data.get(feature, 0)

    # --------------------------------------------------
    # Gender
    # --------------------------------------------------

    if customer_data.get("Gender") == "Male":
        processed_data["Gender_Male"] = 1

    # --------------------------------------------------
    # Yes / No Features
    # --------------------------------------------------

    yes_no_features = [
        "Partner",
        "Dependents",
        "PhoneService"
    ]

    for feature in yes_no_features:
        if customer_data.get(feature) == "Yes":
            processed_data[f"{feature}_Yes"] = 1

    # --------------------------------------------------
    # Internet Service
    # --------------------------------------------------

    internet_service = customer_data.get("InternetService")

    if internet_service == "DSL":
        processed_data["InternetService_DSL"] = 1

    elif internet_service == "Fiber Optic":
        processed_data["InternetService_Fiber Optic"] = 1

    elif internet_service == "Unknown":
        processed_data["InternetService_Unknown"] = 1

    # --------------------------------------------------
    # Internet Related Services
    # --------------------------------------------------

    internet_features = [
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies"
    ]

    for feature in internet_features:

        value = customer_data.get(feature)

        if value == "Yes":
            processed_data[f"{feature}_Yes"] = 1

        elif value == "No internet service":
            processed_data[
                f"{feature}_No internet service"
            ] = 1

    # --------------------------------------------------
    # Contract
    # --------------------------------------------------

    contract = customer_data.get("Contract")

    if contract == "One year":
        processed_data["Contract_One year"] = 1

    elif contract == "Two year":
        processed_data["Contract_Two year"] = 1

    # Month-to-month is represented by both columns = 0

    # --------------------------------------------------
    # Payment Method
    # --------------------------------------------------

    payment_method = customer_data.get("PaymentMethod")

    if payment_method == "Credit Card":
        processed_data["PaymentMethod_Credit Card"] = 1

    elif payment_method == "Electronic Check":
        processed_data["PaymentMethod_Electronic Check"] = 1

    elif payment_method == "Mailed Check":
        processed_data["PaymentMethod_Mailed Check"] = 1

    # --------------------------------------------------
    # Tenure Group
    # --------------------------------------------------

    tenure = customer_data.get("TenureMonths", 0)

    if 12 <= tenure < 24:
        processed_data["TenureGroup_1-2 Years"] = 1

    elif 24 <= tenure < 48:
        processed_data["TenureGroup_2-4 Years"] = 1

    elif tenure >= 48:
        processed_data["TenureGroup_4-6 Years"] = 1

    # 0-1 year is represented by all tenure group columns = 0

    # --------------------------------------------------
    # Monthly Charge Category
    # --------------------------------------------------

    monthly_charges = customer_data.get(
        "MonthlyCharges",
        0
    )

    if monthly_charges < 40:
        processed_data["MonthlyChargeCategory_Low"] = 1

    elif monthly_charges < 80:
        processed_data["MonthlyChargeCategory_Medium"] = 1

    # High monthly charge is represented by both columns = 0

    # --------------------------------------------------
    # Support Level
    # --------------------------------------------------

    support_tickets = customer_data.get(
        "SupportTickets",
        0
    )

    if support_tickets <= 2:
        processed_data["SupportLevel_Low"] = 1

    elif support_tickets <= 5:
        processed_data["SupportLevel_Medium"] = 1

    # High support level is represented by both columns = 0

    return processed_data