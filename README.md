# Finance-AI-for-stocks
The Stock Prediction Web Application is a user-friendly tool that allows users to analyze historical stock data, visualize trends, and make future predictions for selected stocks.
# Features:
## 1. Stock Data Analysis:
Users can choose from a list of popular stocks, including well-known companies like Apple (AAPL), Google (GOOG), Microsoft (MSFT), and GameStop (GME). The application fetches historical stock data using the Yahoo Finance API, providing users with insights into the stock's opening and closing prices over a specified period.

## 2. Time Series Data Visualization:
The application displays the raw time series data using interactive charts powered by Plotly. Users can easily visualize the trends in stock opening and closing prices over the selected timeframe.

## 3. Profitability Analysis:
The tool calculates the profitability of each stock by analyzing the percentage change in closing prices. A pie chart is generated to visually represent the distribution of profitability among the selected stocks. The application uses text-to-speech technology to provide users with an audible overview of the profitability distribution.

## 4. Forecasting with Prophet:
The application utilizes Facebook Prophet, a forecasting tool, to predict future stock prices based on historical data. Users can adjust the prediction period using a slider, and the tool generates forecasts along with component visualizations (trend, seasonality) for better understanding.


# Technologies Used:
Streamlit: For building the interactive web application.
Plotly: For creating interactive and visually appealing charts.
Yahoo Finance API: To fetch historical stock data.
Facebook Prophet: For time series forecasting.
pyttsx3: For text-to-speech functionality.
Future Enhancements:
Incorporate more advanced machine learning models for prediction.
Add sentiment analysis of news and social media data for improved forecasting.
Include real-time stock data updates.

# Conclusion:
The Stock Prediction Web Application provides users with valuable insights into historical stock data, profitability analysis, and future price predictions. Whether you are a stock enthusiast or an investor, this tool can help you make informed decisions based on data-driven analysis.
