# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import calculate_financial_score

app = FastAPI()

# Input schema
class FamilyData(BaseModel):
    Income: float
    Savings: float
    Monthly_Expenses: float
    Loan_Payments: float
    Credit_Card_Spending: float
    Financial_Goals_Met: float

@app.get("/")
def home():
    return {"message": "Welcome to the Financial Scoring API!"}

@app.post("/calculate_score/")
def calculate_score(data: FamilyData):
    try:
        # Map input keys to expected column names
        input_data = {
            "Income": data.Income,
            "Savings": data.Savings,
            "Monthly Expenses": data.Monthly_Expenses,  # Match exact column name
            "Loan Payments": data.Loan_Payments,       # Match exact column name
            "Credit Card Spending": data.Credit_Card_Spending,  # Match exact column name
            "Financial Goals Met (%)": data.Financial_Goals_Met  # Match exact column name
        }

        # Calculate financial score
        result = calculate_financial_score(input_data)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
