# KUBER 📈💸

## Description
KUBER is a Python script that utilizes the Alpha Vantage API and the forex-python library to fetch historical stock data, perform a linear regression-based prediction for the next 7 days, and convert the predicted close prices to Indian Rupees (INR).

## Prerequisites
Make sure you have the required libraries installed:
```bash
pip3 install requests pandas scikit-learn forex-python
```

## Usage
1. Run the script:
   ```bash
   python3 main.py
   ```
2. Enter the stock symbol when prompted (e.g., AAPL).
3. View the predictions for the next 7 days, including the predicted close prices in INR.

## Features
- Fetches stock data from Alpha Vantage API.
- Uses linear regression for stock price prediction.
- Converts predicted prices to INR using the forex-python library.

## Configuration
Replace the `api_key` variable in the script with your Alpha Vantage API key.

## Contributing
Contributions are welcome! If you find any issues or have improvements, feel free to create a pull request.

## Credits
- [Alpha Vantage](https://www.alphavantage.co/) for providing stock market data.
- [forex-python](https://github.com/MicroPyramid/forex-python) for currency exchange rate conversion.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
