import yfinance as yf
import pandas as pd
import os

# Create output directory
output_dir = "mag7_daily_data"
os.makedirs(output_dir, exist_ok=True)

# Mag7 tickers
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "NVDA", "TSLA"]

# Date range
start_date = "2000-01-01"
end_date = pd.Timestamp.today().strftime('%Y-%m-%d')

# Download daily data and save each to its own CSV
for ticker in tickers:
    print(f"⏳ Downloading {ticker}...")
    df = yf.download(ticker, start=start_date, end=end_date, interval="1d")
    df.dropna(inplace=True)
    df.to_csv(f"{output_dir}/{ticker}_daily.csv")
    print(f"✅ Saved {ticker}_daily.csv")

print("\n📁 All daily data files saved in 'mag7_daily_data' folder.")
