import pandas as pd

def get_features():
    df = pd.read_csv("data/processed/feature_store.csv")
    return df