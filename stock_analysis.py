import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def download_stock_data(ticker, start_date, end_date):
    stock = yf.download(ticker, start=start_date, end=end_date)
    return stock

def calculate_moving_average(data, window_size):
    return data['Close'].rolling(window=window_size).mean()

def calculate_daily_return(data):
    return data['Close'].pct_change()

def plot_data(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], label='Closing Price')
    plt.plot(data.index, data['Moving_Average_50'], label='50-day Moving Average')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    data = download_stock_data("AAPL", "2022-01-01", "2023-01-01")
    data['Moving_Average_50'] = calculate_moving_average(data, 50)
    data['Daily_Return'] = calculate_daily_return(data)
    print(data.head())





