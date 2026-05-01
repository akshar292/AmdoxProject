from backend.api.utils import get_model_path
import joblib
import numpy as np

MODEL_PATH = get_model_path("kmeans.pkl")
print(f"📦 Loading segmentation model from: {MODEL_PATH}")

model = joblib.load(MODEL_PATH)

def score_segment(req):
    try:
        X = np.array([[req.feature1, req.feature2, req.feature3]])
        pred = model.predict(X)[0]

        return {"segment": int(pred)}
    except Exception as e:
        return {"error": str(e)}