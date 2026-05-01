import pandas as pd

def load_pricing_data():
    print("📂 Loading pricing data...")

    df = pd.read_csv("data/processed/pricing_data.csv")

    print("Columns:", df.columns)
    print(df.head())

    return df