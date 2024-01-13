import streamlit as st
from datetime import date
import yfinance as yf
import plotly
from plotly import graph_objs as go
import functools
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import plotly.express as px
import pyttsx3

Start = "2010-01-01"
Today = date.today().strftime("%Y-%m-%d")

st.title("Stock App")
stocks = ("AAPL", "GOOG", "MSFT", "GME", "AMZN", "NFLX", "TSLA", "FB", "GOOGL", "NVDA", "V", "PYPL", "INTC", "AMD", "CSCO", "IBM", "GS", "JPM", "BAC", "DIS", "IBM", "VZ", "KO", "PEP", "MCD", "WMT")
selected_stock = st.selectbox("Select dataset for prediction", stocks)
n_years = st.slider("Year:", 1, 4)
period = n_years * 365

# Use functools.lru_cache decorator for caching
@functools.lru_cache(maxsize=None)
def load_data(ticker):
    data = yf.download(ticker, Start, Today)
    data.reset_index(inplace=True)
    return data

data_load_state = st.text("Load Data ......")
data = load_data(selected_stock)
data_load_state.text("Loading Data.... Done")

st.subheader("Raw Data")
st.write(data.tail())

def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
    fig.update_layout(title_text="Time Series Data", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()

def news():
    url = "https://finance.yahoo.com/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    news_titles = soup.find_all("h3", class_= "Mb(5px)")
    news_links = soup.find_all("a", class_= "Fw(b)")

    finance_news = [{"title": title.text, "link": "https://finance.yahoo.com/news/" + link.get("href")} for title,link in zip(news_titles, news_links)]
    return finance_news

st.title("Finance News")
page_load_state = st.text("Load Financial News ......")

finance_news = news()
for new in finance_news:
    st.write(f"[{new['title']}] ({new['link']})")


def get_stock_profit(stock_symbol):
    stock = yf.Ticker(stock_symbol)
    historical_data = stock.history(period="1y")
    initial_price = historical_data['Close'].iloc[0]
    final_price = historical_data['Close'].iloc[-1]

    profit_percentage = ((final_price - initial_price) / initial_price) * 100
    return profit_percentage

st.title("Stock Profit Predictor")
stock_symbol = st.text_input("Enter Stock Symbol (e.g., AAPL for Apple):")
if st.button("Predict Profit"):
    if not stock_symbol:
        st.warning("Please enter a valid stock symbol.")
    else:
        try:
            profit_percentage = get_stock_profit(stock_symbol.upper())
            st.success(f"The predicted profit for {stock_symbol.upper()} is: {profit_percentage:.2f}%")
        except Exception as e:
            st.error(f"Error: {str(e)}")

# for running
# cd {your file location}
# streamlit run {name of the file}
