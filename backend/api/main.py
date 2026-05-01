from fastapi import FastAPI, Depends
from backend.api.schemas import (
    DemandRequest, InventoryRequest
)
from backend.api.auth import verify_api_key
from backend.api.services.demand import predict_demand
from backend.api.services.inventory import reorder_suggestion

app = FastAPI(title="NeuralRetail Scoring API")

# ---------------- HEALTH ----------------
@app.get("/health")
def health():
    return {"status": "ok"}

# ---------------- DEMAND ----------------
@app.post("/predict/demand")
def demand(req: DemandRequest, user=Depends(verify_api_key)):
    return predict_demand(req)

# ---------------- INVENTORY ----------------
@app.post("/inventory/reorder")
def inventory(req: InventoryRequest):
    return reorder_suggestion(req)