import pandas as pd
import os

def clean_mag7_data(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "NVDA", "TSLA"]

    for ticker in tickers:
        input_file = os.path.join(input_folder, f"{ticker}_daily.csv")
        output_file = os.path.join(output_folder, f"{ticker}_daily_cleaned.csv")
        
        try:
            # Load and skip the extra header rows
            df = pd.read_csv(input_file, skiprows=2)
            df.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']

            # Convert numeric columns
            for col in ['Open', 'Close', 'Low', 'High']:
                df[col] = pd.to_numeric(df[col], errors='coerce')

            # Drop rows with missing data
            df.dropna(subset=['Open', 'Close', 'Low', 'High'], inplace=True)

            # Calculate rate-of-change columns
            df['O2C'] = (df['Close'] - df['Open']) / df['Open']
            df['O2L'] = (df['Low'] - df['Open']) / df['Open']
            df['O2H'] = (df['High'] - df['Open']) / df['Open']

            # Save cleaned data
            df.to_csv(output_file, index=False)
            print(f"✅ Cleaned: {ticker} → {output_file}")
        
        except Exception as e:
            print(f"❌ Error processing {ticker}: {e}")

# Example usage
input_dir = "mag7_daily_data"              # Folder with raw Mag7 CSVs
output_dir = "mag7_daily_cleaned_data"     # Folder to save cleaned files

#clean_mag7_data(input_dir, output_dir)


def clean_weekly_csv(file_path, output_path=None):
    # Skip the first two rows
    df = pd.read_csv(file_path, skiprows=2)
    
    # Rename columns
    df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'O2C', 'O2L', 'O2H']
    
    # Optional: save to new file
    if output_path is None:
        output_path = file_path.replace(".csv", "_final.csv")
    
    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned and saved: {output_path}")

# Example usage
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "NVDA", "TSLA"]
for ticker in tickers:
    input_file = f"mag7_weekly_cleaned_data/{ticker}_weekly_cleaned.csv"
    clean_weekly_csv(input_file)
