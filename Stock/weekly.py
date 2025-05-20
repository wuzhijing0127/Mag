import yfinance as yf
import pandas as pd
import os

def download_and_clean_weekly_mag7(output_folder):
    os.makedirs(output_folder, exist_ok=True)

    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "NVDA", "TSLA"]
    start_date = "2000-01-01"
    end_date = pd.Timestamp.today().strftime('%Y-%m-%d')

    for ticker in tickers:
        print(f"📥 Downloading {ticker} weekly data...")
        try:
            # Download weekly OHLCV data
            df = yf.download(ticker, start=start_date, end=end_date, interval="1wk")

            # Drop missing data
            df.dropna(inplace=True)

            # Drop unwanted columns
            df = df.drop(columns=["Volume", "Adj Close"], errors='ignore')

            # Calculate change rates
            df['O2C'] = (df['Close'] - df['Open']) / df['Open']
            df['O2L'] = (df['Low'] - df['Open']) / df['Open']
            df['O2H'] = (df['High'] - df['Open']) / df['Open']

            # Reorder columns
            df = df[['Open', 'High', 'Low', 'Close', 'O2C', 'O2L', 'O2H']]

            # Save to CSV
            df.to_csv(os.path.join(output_folder, f"{ticker}_weekly_cleaned.csv"))
            print(f"✅ Saved cleaned file: {ticker}_weekly_cleaned.csv")

        except Exception as e:
            print(f"❌ Error with {ticker}: {e}")

# Example usage
output_dir = "mag7_weekly_cleaned_data"
download_and_clean_weekly_mag7(output_dir)
