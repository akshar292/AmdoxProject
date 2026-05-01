import pandas as pd
from backend.segmentation.prepare_rfm import create_rfm


def load_data():
    print("📂 Loading data...")
    df = pd.read_csv("data/processed/feature_store.csv")
    return df


def run_segmentation_pipeline():

    print("🚀 Running Customer Segmentation Pipeline...")

    df = load_data()

    print("📂 Raw Data Columns:", df.columns)
    print(df.head())

    rfm = create_rfm(df)

    print("✅ Pipeline working till RFM stage")


if __name__ == "__main__":
    print("🔥 ENTRY POINT HIT")
    run_segmentation_pipeline()