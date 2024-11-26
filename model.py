import pandas as pd

def calculate_financial_score(data):
    df = pd.DataFrame([data])  # Convert input to DataFrame
    
    # Normalize ratios
    df['Savings Ratio'] = df['Savings'] / df['Income']
    df['Expense Ratio'] = df['Monthly Expenses'] / df['Income']
    df['Loan Ratio'] = df['Loan Payments'] / df['Income']
    df['Credit Spending Ratio'] = df['Credit Card Spending'] / df['Income']
    df['Financial Goals Met'] = df['Financial Goals Met (%)'] / 100  # Convert to 0–1 scale

    # Calculate financial score
    df['FinancialScore'] = (
        (df['Savings Ratio'] * 40) +
        (df['Financial Goals Met'] * 20) -
        (df['Expense Ratio'] * 15) -
        (df['Loan Ratio'] * 15) -
        (df['Credit Spending Ratio'] * 10)
    ).clip(0, 100)  # Ensure score is between 0 and 100

    # Extract insights with adjusted thresholds
    insights = []
    if df['Savings Ratio'][0] < 0.25:
        insights.append("Savings ratio is below 25%, consider saving more.")
    if df['Expense Ratio'][0] > 0.25:
        insights.append("Expenses exceed 25% of income, consider reducing spending.")
    if df['Loan Ratio'][0] > 0.15:
        insights.append("Loan payments exceed 15% of income, consider paying off loans faster.")
    
    return {
        "FinancialScore": df['FinancialScore'][0],
        "Insights": insights
    }
