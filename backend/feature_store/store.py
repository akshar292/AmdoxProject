import pandas as pd

def save_features(df):
    df.to_csv("data/processed/feature_store.csv", index=False)
    print("Feature store saved ✅")