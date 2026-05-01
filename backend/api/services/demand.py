import joblib
import numpy as np
from backend.api.utils import get_model_path

model = None

def load_model():
    global model
    if model is None:
        MODEL_PATH = get_model_path("demand_model.pkl")
        print(f"📦 Loading demand model from: {MODEL_PATH}")
        model = joblib.load(MODEL_PATH)
    return model


def predict_demand(req):
    try:
        model = load_model()

        X = np.array([[req.price, req.promo_flag, req.season]])
        pred = model.predict(X)[0]

        return {"predicted_demand": float(pred)}

    except Exception as e:
        return {"error": str(e)}