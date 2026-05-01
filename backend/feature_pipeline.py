import pandas as pd

from features.date_features import create_date_features

def run_feature_pipeline():
    df = pd.read_csv("data/processed/clean_data.csv")

    print(df.columns)  # optional

    df = create_date_features(df)

    # skip rolling & lag for now (dataset doesn't support properly)
    df = df.fillna(0)

    df.to_csv("data/processed/feature_data.csv", index=False)

    print("Feature pipeline completed ✅")

if __name__ == "__main__":
    run_feature_pipeline()