import streamlit as st
import requests

# FastAPI URL for financial score calculation
API_URL = "http://127.0.0.1:8000/calculate_score/"

# Streamlit form for financial data input
st.title("Financial Score & Insights Calculator")

st.write("Enter your family's financial data below:")

# Empty input fields using st.empty() for placeholders
income = st.number_input("Income", min_value=1000, step=1000, value=None)
savings = st.number_input("Savings", min_value=0, step=1000, value=None)
monthly_expenses = st.number_input("Monthly Expenses", min_value=0, step=1000, value=None)
loan_payments = st.number_input("Loan Payments", min_value=0, step=1000, value=None)
credit_card_spending = st.number_input("Credit Card Spending", min_value=0, step=500, value=None)
financial_goals_met = st.slider("Financial Goals Met (%)", min_value=0, max_value=100, value=0)

# Button to trigger financial score calculation
if st.button("Calculate Financial Score and Insights"):
    # Check if any required fields are empty
    if income is None or savings is None or monthly_expenses is None or loan_payments is None or credit_card_spending is None:
        st.error("Please fill in all the fields before submitting.")
    else:
        # Prepare data for API
        data = {
            "Income": income,
            "Savings": savings,
            "Monthly_Expenses": monthly_expenses,
            "Loan_Payments": loan_payments,
            "Credit_Card_Spending": credit_card_spending,
            "Financial_Goals_Met": financial_goals_met
        }

        # Make API request to FastAPI
        response = requests.post(API_URL, json=data)

        if response.status_code == 200:
            result = response.json()

            # Display results
            st.subheader(f"Financial Score: {result['FinancialScore']}")
            if result['Insights']:
                st.write("### Insights:")
                for insight in result['Insights']:
                    st.write(f"- {insight}")
            else:
                st.write("### No insights to display. Your financial health looks good!")
        else:
            st.error("Error in calculating financial score. Please try again.")
