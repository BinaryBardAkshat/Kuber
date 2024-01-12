import requests
import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import datetime

# Replace 'YOUR_API_KEY' with your Alpha Vantage API key
api_key = '2XD46Q5F18KAG4HA'

# Function to fetch stock data from Alpha Vantage
def get_stock_data(symbol, api_key):
    base_url = 'https://www.alphavantage.co/query'
    function = 'TIME_SERIES_DAILY'
    outputsize = 'full'

    params = {
        'function': function,
        'symbol': symbol,
        'apikey': api_key,
        'outputsize': outputsize
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    time_series = data['Time Series (Daily)']

    df = pd.DataFrame(time_series).T
    df.index = pd.to_datetime(df.index)
    df.sort_index(inplace=True)

    return df

# Function to predict stock price for the next 7 days using linear regression
def predict_stock_price(df):
    df['Date'] = df.index
    df['Date'] = df['Date'].map(datetime.datetime.toordinal)

    X = df[['Date']]
    y = df['4. close']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    last_date = df.index[-1].toordinal() + 1
    future_dates = [last_date + i for i in range(1, 8)]
    future_dates = pd.DataFrame(future_dates, columns=['Date'])

    predictions = model.predict(future_dates)

    return predictions

# Main function
def main():
    user_symbol = input("Enter the stock symbol (e.g., AAPL): ").upper()
    stock_data = get_stock_data(user_symbol, api_key)

    if stock_data.empty:
        print(f"No data found for the stock symbol: {user_symbol}")
        return

    predictions = predict_stock_price(stock_data)

    print(f"\nStock Data for {user_symbol}:")
    print(stock_data.tail())

    print("\nPredictions for the next 7 days:")
    for i, prediction in enumerate(predictions):
        date = (datetime.datetime.fromordinal(int(prediction))).strftime('%Y-%m-%d')
        print(f"Day {i+1}: {date}, Predicted Close Price: {prediction:.2f}")

if __name__ == "__main__":
    main()
