import pandas as pd
from sklearn.cluster import KMeans
import joblib
import os

print("📂 Loading data...")

df = pd.read_csv("data/processed/feature_store.csv")

# Example features
X = df[["month", "week_of_year", "day_of_week"]]

print("🤖 Training KMeans...")

model = KMeans(n_clusters=3, random_state=42)
model.fit(X)

# Save model
os.makedirs("backend/models", exist_ok=True)
joblib.dump(model, "backend/models/kmeans.pkl")

print("✅ Segmentation model saved!")