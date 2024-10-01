# Stock Analysis Lambda Function

This repository contains a Python project for analyzing stock data, built for deployment on AWS Lambda. The project fetches stock price data using the `yfinance` library, performs data manipulation using `pandas`, and can be deployed as a serverless function using AWS Lambda.

## Project Overview

This project allows you to download stock data, calculate key financial indicators (such as moving averages and daily returns), and plot the results. Originally intended to be deployed as an AWS Lambda function, the project can run locally or in a serverless environment.

### Features
- Fetch stock data from Yahoo Finance using `yfinance`.
- Calculate moving averages and daily returns using `pandas`.
- Plot closing prices and moving averages using `matplotlib`.
- Packaged and optimized for deployment on AWS Lambda.

## Requirements

The project requires the following Python packages:

- `pandas`: Data manipulation and analysis.
- `yfinance`: To fetch stock data from Yahoo Finance.
- `matplotlib`: Plotting stock data (optional for AWS Lambda but useful locally).

You can install the required dependencies by running:

```bash
pip install -r requirements.txt
```

## Project Structure


The repository includes the following files:

- `stock_analysis.py`: Main Python script that fetches stock data and performs analysis.
- `requirements.txt`: File listing all the dependencies required for the project.
- `.gitignore`: Git ignore file for ignoring virtual environments and other unnecessary files.

### Main Python Script (`stock_analysis.py`)

The `stock_analysis.py` script performs the following:

1. **Download Stock Data**:
    - Using the `yfinance` library, the script downloads stock data for a specified ticker and time period.
    
    ```python
    def download_stock_data(ticker, start_date, end_date):
        stock = yf.download(ticker, start=start_date, end=end_date)
        return stock
    ```

2. **Calculate Financial Indicators**:
    - The script calculates the 50-day moving average and daily returns using `pandas` functions.

    ```python
    def calculate_moving_average(data, window_size):
        return data['Close'].rolling(window=window_size).mean()

    def calculate_daily_return(data):
        return data['Close'].pct_change()
    ```

3. **Plot the Data**:
    - Plots the stock’s closing price and its 50-day moving average.

    ```python
    def plot_data(data):
        plt.figure(figsize=(12, 6))
        plt.plot(data.index, data['Close'], label='Closing Price')
        plt.plot(data.index, data['Moving_Average_50'], label='50-day Moving Average')
        plt.legend()
        plt.show()
    ```

4. **AWS Lambda Handler**:
    - The script includes a `lambda_handler` function for AWS Lambda deployment. This function can fetch stock data based on event input and return the result as a JSON response.

    ```python
    def lambda_handler(event, context):
        ticker = event.get('ticker', 'AAPL')
        start_date = event.get('start_date', '2022-01-01')
        end_date = event.get('end_date', '2023-01-01')

        stock_data = download_stock_data(ticker, start_date, end_date)
        return {
            'statusCode': 200,
            'body': stock_data.to_dict()
        }
    ```

## How to Run Locally

You can run this project locally to fetch stock data and visualize it.

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/stock-analysis.git
    cd stock-analysis
    ```

2. **Set up a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the script**:

    ```bash
    python stock_analysis.py
    ```

   The script will download stock data for Apple Inc. (AAPL) and calculate its 50-day moving average and daily returns. It will then plot the closing price and moving average.

## AWS Lambda Deployment (Optional)

If you want to deploy this function on AWS Lambda, follow these steps:

1. **Package the code and dependencies**:
    - If using AWS Lambda, package the code and its dependencies into a ZIP file.
    
    ```bash
    zip -r9 lambda_function.zip .
    ```

2. **Create an AWS Lambda Function**:
    - Use the AWS CLI or the Lambda console to create a Lambda function. Set the handler to `stock_analysis.lambda_handler`.

3. **Upload the deployment package**:
    - Upload the `lambda_function.zip` to your AWS Lambda function.

4. **Invoke the Lambda Function**:
    - You can invoke the Lambda function by passing in the stock ticker and date range as part of the event.

## Future Improvements
- Add additional financial metrics (e.g., exponential moving averages, Bollinger Bands).
- Implement real-time data fetching using scheduled Lambda invocations.
- Explore integration with AWS services like S3 and CloudWatch for enhanced data storage and monitoring.


