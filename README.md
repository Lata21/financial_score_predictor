# **Financial Score & Insights Calculator App**

This project is a **Streamlit** app that allows users to calculate their **financial score** and receive **personalized insights** based on their financial data. The backend is powered by **FastAPI** to process the calculations and provide insights.

### **Features**:
- **Financial Score Calculation**: Based on the ratio of savings, expenses, loans, and credit card spending relative to income.
- **Insights Generation**: Offers recommendations based on user input, such as saving more, reducing spending, or paying off loans faster.
- **Interactive UI**: Built with Streamlit for easy data entry and visualization.

---

## **Technologies Used**:
- **Frontend**: Streamlit
- **Backend**: FastAPI
- **Data Processing**: Pandas
- **Deployment**: Locally using Uvicorn and Streamlit

---

## **Installation**:

### **1. Install the Required Packages**:

#### Backend (FastAPI):
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/financial-score-app.git
   cd financial-score-app
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install FastAPI and Uvicorn for the backend:
   ```bash
   pip install fastapi uvicorn pandas
   ```

#### Frontend (Streamlit):
5. Install Streamlit for the frontend:
   ```bash
   pip install streamlit requests
   ```

---

## **Running the App**:

### **1. Run the FastAPI Backend**:
- The backend calculates the financial score and insights. Run it using **Uvicorn**:
   ```bash
   uvicorn main:app --reload
   ```

   This will start the FastAPI server on `http://127.0.0.1:8000`.

### **2. Run the Streamlit Frontend**:
- In another terminal window, navigate to the directory containing the `streamlit_app.py` file and run:
   ```bash
   streamlit run streamlit_app.py
   ```

   This will start the Streamlit app on `http://localhost:8501`.

---

## **How to Use**:

1. **Open the Streamlit App**: After running the Streamlit app, open your browser and go to `http://localhost:8501`.
   
2. **Input Financial Data**:
   - Enter values for **Income**, **Savings**, **Monthly Expenses**, **Loan Payments**, **Credit Card Spending**, and **Financial Goals Met**.
   - The fields are initially empty, and you need to input your own values.

3. **Click "Calculate Financial Score and Insights"**: Once you’ve entered your data, click the button to calculate your financial score and get personalized insights based on the input data.

4. **View Results**: 
   - The app will display your **financial score**.
   - If there are any insights, they will be displayed under the score (e.g., suggestions to save more, reduce spending, or pay off loans).

---

## **Example Input and Output**:

### **Example 1: Typical Family with Balanced Financial Health**
**Input**:
- Income: `75000`
- Savings: `15000`
- Monthly Expenses: `20000`
- Loan Payments: `5000`
- Credit Card Spending: `1500`
- Financial Goals Met: `80`

**Output**:
```json
{
    "FinancialScore": 18.8,
    "Insights": [
        "Savings ratio is below 25%, consider saving more.",
        "Expenses exceed 25% of income, consider reducing spending."
    ]
}
```

### **Example 2: High Expenses and Low Savings**
**Input**:
- Income: `60000`
- Savings: `5000`
- Monthly Expenses: `45000`
- Loan Payments: `5000`
- Credit Card Spending: `3000`
- Financial Goals Met: `50`

**Output**:
```json
{
    "FinancialScore": 0.33,
    "Insights": [
        "Savings ratio is below 25%, consider saving more.",
        "Expenses exceed 25% of income, consider reducing spending."
    ]
}
```

---

## **API Documentation**:

1. **Endpoint**: `/calculate_score/`
2. **Method**: `POST`
3. **Request Body**:
   ```json
   {
       "Income": 75000,
       "Savings": 15000,
       "Monthly_Expenses": 20000,
       "Loan_Payments": 5000,
       "Credit_Card_Spending": 1500,
       "Financial_Goals_Met": 80
   }
   ```

4. **Response**:
   ```json
   {
       "FinancialScore": 18.8,
       "Insights": [
           "Savings ratio is below 25%, consider saving more.",
           "Expenses exceed 25% of income, consider reducing spending."
       ]
   }
   ```

You can also test the FastAPI backend directly by going to `http://127.0.0.1:8000/docs`, where FastAPI provides interactive API documentation.


