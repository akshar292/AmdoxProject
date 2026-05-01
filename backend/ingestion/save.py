import os

def save_data(df):
    os.makedirs("data/processed", exist_ok=True)  # create folder if not exists
    df.to_csv("data/processed/clean_data.csv", index=False)
    print("Data saved ✅")