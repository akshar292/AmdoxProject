import pandas as pd

from feature_store.store import save_features
from data_quality.checks import run_checks

def run_feature_store_pipeline():
    df = pd.read_csv("data/processed/feature_data.csv")

    run_checks(df)
    save_features(df)

    print("Feature Store Pipeline Completed ✅")

if __name__ == "__main__":
    run_feature_store_pipeline()