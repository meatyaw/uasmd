import streamlit as st

from src.inference import CreditScorePredictor


predictor = CreditScorePredictor("best_model.pkl")

st.set_page_config(
    page_title="Credit Score Prediction",
    layout="centered"
)

st.title("Credit Score Prediction")

st.write(
    "Masukkan data pelanggan untuk memprediksi Credit Score."
)

month = st.selectbox(
    "Month",
    [
        "January","February","March","April",
        "May","June","July","August",
        "September","October","November","December"
    ]
)

age = st.number_input("Age", min_value=18)

annual_income = st.number_input(
    "Annual Income",
    min_value=0.0
)

monthly_salary = st.number_input(
    "Monthly Inhand Salary",
    min_value=0.0
)

num_bank_accounts = st.number_input(
    "Number of Bank Accounts",
    min_value=0
)

num_credit_card = st.number_input(
    "Number of Credit Cards",
    min_value=0
)

interest_rate = st.number_input(
    "Interest Rate",
    min_value=0.0
)

num_loan = st.number_input(
    "Number of Loans",
    min_value=0
)

delay_due = st.number_input(
    "Delay from Due Date",
    min_value=0
)

delayed_payment = st.number_input(
    "Number of Delayed Payment",
    min_value=0
)

changed_credit_limit = st.number_input(
    "Changed Credit Limit"
)

credit_inquiries = st.number_input(
    "Credit Inquiries",
    min_value=0
)

credit_mix = st.selectbox(
    "Credit Mix",
    [
        "Bad",
        "Standard",
        "Good"
    ]
)

outstanding_debt = st.number_input(
    "Outstanding Debt",
    min_value=0.0
)

credit_utilization = st.number_input(
    "Credit Utilization Ratio",
    min_value=0.0
)

credit_history = st.text_input(
    "Credit History Age",
    "22 Years and 5 Months"
)

payment_min = st.selectbox(
    "Payment of Minimum Amount",
    [
        "Yes",
        "No"
    ]
)

total_emi = st.number_input(
    "Total EMI per Month",
    min_value=0.0
)

amount_invested = st.number_input(
    "Amount Invested Monthly",
    min_value=0.0
)

payment_behaviour = st.selectbox(
    "Payment Behaviour",
    [
        "High_spent_Small_value_payments",
        "Low_spent_Small_value_payments",
        "High_spent_Medium_value_payments",
        "Low_spent_Medium_value_payments",
        "High_spent_Large_value_payments",
        "Low_spent_Large_value_payments"
    ]
)

monthly_balance = st.number_input(
    "Monthly Balance"
)

if st.button("Predict"):

    data = {

        "Month": month,
        "Age": age,
        "Annual_Income": annual_income,
        "Monthly_Inhand_Salary": monthly_salary,
        "Num_Bank_Accounts": num_bank_accounts,
        "Num_Credit_Card": num_credit_card,
        "Interest_Rate": interest_rate,
        "Num_of_Loan": num_loan,
        "Delay_from_due_date": delay_due,
        "Num_of_Delayed_Payment": delayed_payment,
        "Changed_Credit_Limit": changed_credit_limit,
        "Num_Credit_Inquiries": credit_inquiries,
        "Credit_Mix": credit_mix,
        "Outstanding_Debt": outstanding_debt,
        "Credit_Utilization_Ratio": credit_utilization,
        "Credit_History_Age": credit_history,
        "Payment_of_Min_Amount": payment_min,
        "Total_EMI_per_month": total_emi,
        "Amount_invested_monthly": amount_invested,
        "Payment_Behaviour": payment_behaviour,
        "Monthly_Balance": monthly_balance

    }

    prediction = predictor.predict(data)

    st.success(f"Prediction : {prediction}")