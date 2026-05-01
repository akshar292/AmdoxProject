import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestClassifier

def train_churn():
    df = pd.read_csv("data/processed/feature_store.csv")

    df["churn"] = (df["month"] > 6).astype(int)

    X = df[["day_of_week", "week_of_year", "month"]]
    y = df["churn"]

    model = RandomForestClassifier()
    model.fit(X, y)

    os.makedirs("backend/models", exist_ok=True)
    joblib.dump(model, "backend/models/churn_model.pkl")

    print("✅ Churn model saved")

if __name__ == "__main__":
    train_churn()