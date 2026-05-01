import pandas as pd
import os

def load_churn_data():
    print("📂 Loading churn data...")

    # Get project root dynamically
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

    file_path = os.path.join(BASE_DIR, "data", "processed", "feature_store.csv")

    print("Using path:", file_path)

    df = pd.read_csv(file_path)

    # Example target (modify if needed)
    df['event'] = df['event'].map({
        'view': 0,
        'addtocart': 1,
        'transaction': 2
    })

    X = df[['day_of_week', 'week_of_year', 'month']]
    y = df['event']

    return X, y