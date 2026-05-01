import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def train_demand_model():

    print("📂 Loading data...")

    df = pd.read_csv("data/processed/feature_store.csv")

    # Create features
    df["price"] = 100  # dummy
    df["promo_flag"] = 0
    df["season"] = df["month"]

    # Target
    df["demand"] = 200 - 0.5 * df["price"]

    X = df[["price", "promo_flag", "season"]]
    y = df["demand"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("🤖 Training model...")

    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    # ✅ SAVE MODEL
    os.makedirs("backend/models", exist_ok=True)
    joblib.dump(model, "backend/models/demand_model.pkl")

    print("✅ Model saved successfully!")


if __name__ == "__main__":
    train_demand_model()