from .prepare_data import load_churn_data
from .train_xgb import train_xgb
from .evaluate import evaluate_model

def run_churn_pipeline():

    print("🚀 Running Churn Model...")

    X, y = load_churn_data()

    model, X_test, y_test = train_xgb(X, y)

    evaluate_model(model, X_test, y_test)

    print("Churn model completed ✅")


if __name__ == "__main__":
    run_churn_pipeline()