import pandas as pd
import joblib
import os
from sklearn.cluster import KMeans

def train_segmentation():
    df = pd.read_csv("data/processed/feature_store.csv")

    X = df[["day_of_week", "month"]]

    model = KMeans(n_clusters=3)
    model.fit(X)

    os.makedirs("backend/models", exist_ok=True)
    joblib.dump(model, "backend/models/kmeans.pkl")

    print("✅ Segmentation model saved")

if __name__ == "__main__":
    train_segmentation()