import xgboost as xgb
from sklearn.model_selection import train_test_split

def train_xgb(X, y):

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Handle imbalance
    ratio = (y == 0).sum() / (y == 1).sum()

    model = xgb.XGBClassifier(
        n_estimators=200,
        max_depth=6,
        learning_rate=0.05,
        scale_pos_weight=ratio,   # ✅ ONLY ONCE
        random_state=42,
        eval_metric="logloss"
    )

    model.fit(X_train, y_train)

    return model, X_test, y_test