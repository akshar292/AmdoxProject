import joblib
import numpy as np
from backend.api.utils import get_model_path

model = None

def load_model():
    global model
    if model is None:
        MODEL_PATH = get_model_path("churn_model.pkl")
        print(f"📦 Loading churn model from: {MODEL_PATH}")
        model = joblib.load(MODEL_PATH)
    return model


def predict_churn(req):
    try:
        model = load_model()

        X = np.array([[req.feature1, req.feature2, req.feature3]])
        pred = model.predict(X)[0]

        return {"churn_prediction": int(pred)}

    except Exception as e:
        return {"error": str(e)}