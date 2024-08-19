import streamlit as st
import yfinance as yf
import pandas as pd

# Streamlit page configuration
st.set_page_config(page_title="Stock Analysis", layout="wide")

# Page title
st.title("📈 Stock Analysis")

# Input for the ticker symbol
ticker = st.text_input("Enter a stock ticker (e.g., AAPL, MSFT, TSLA):", "AAPL")

# Fetching the stock data using yfinance
stock = yf.Ticker(ticker)

# Display main stock information
st.header(f"Main Information for {ticker.upper()}")
info = stock.info
st.write(f"**Company Name:** {info.get('longName', 'N/A')}")
st.write(f"**Sector:** {info.get('sector', 'N/A')}")
st.write(f"**Industry:** {info.get('industry', 'N/A')}")
st.write(f"**Market Cap:** ${info.get('marketCap', 'N/A'):,}")
st.write(f"**52 Week High:** ${info.get('fiftyTwoWeekHigh', 'N/A')}")
st.write(f"**52 Week Low:** ${info.get('fiftyTwoWeekLow', 'N/A')}")
st.write(f"**PE Ratio:** {info.get('trailingPE', 'N/A')}")
st.write(f"**Dividend Yield:** {info.get('dividendYield', 'N/A'):.2%}")

# Display historical price data
st.header("Historical Price Data")
period = st.selectbox("Select period:", ['1d', '5d', '1mo', '6mo', '1y', '5y', 'max'], index=5)
data = stock.history(period=period)

st.line_chart(data['Close'])

# Display additional financials (e.g., balance sheet)
st.header(f"Financials for {ticker.upper()}")

# Displaying balance sheet
st.subheader("Balance Sheet")
balance_sheet = stock.balance_sheet
st.dataframe(balance_sheet)

# Displaying income statement
st.subheader("Income Statement")
income_statement = stock.financials
st.dataframe(income_statement)

# Displaying cash flow
st.subheader("Cash Flow")
cash_flow = stock.cashflow
st.dataframe(cash_flow)

# Displaying major holders
st.header("Major Holders")
holders = stock.major_holders
st.dataframe(holders)

# Display recommendations
st.header("Analyst Recommendations")
recommendations = stock.recommendations
st.dataframe(recommendations.tail(10))  # Show the last 10 recommendations

