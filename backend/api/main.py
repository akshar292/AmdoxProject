import time
import logging
import json

from fastapi import FastAPI, Depends, Response
from prometheus_client import Counter, Histogram, generate_latest

from backend.api.schemas import DemandRequest, InventoryRequest
from backend.api.auth import verify_api_key
from backend.api.services.demand import predict_demand
from backend.api.services.inventory import reorder_suggestion


# ---------------- LOGGING SETUP ----------------
logging.basicConfig(level=logging.INFO)


# ---------------- METRICS ----------------
REQUEST_COUNT = Counter("api_requests_total", "Total API Requests")
LATENCY = Histogram("api_latency_seconds", "API Latency")


# ---------------- APP ----------------
app = FastAPI(title="NeuralRetail Scoring API")


# ---------------- HEALTH ----------------
@app.get("/health")
def health():
    return {"status": "ok"}


# ---------------- METRICS ENDPOINT ----------------
@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")


# ---------------- DEMAND ----------------
@app.post("/predict/demand")
def demand(req: DemandRequest, user=Depends(verify_api_key)):

    start = time.time()

    # 🔹 Simple logging
    logging.info("🚀 Demand prediction called")

    # 🔹 Structured JSON logging
    log = {
        "event": "demand_prediction",
        "sku_id": req.sku_id,
        "price": req.price,
        "promo_flag": req.promo_flag,
        "season": req.season,
        "timestamp": time.time()
    }
    print(json.dumps(log))

    # 🔹 Model prediction
    result = predict_demand(req)

    # 🔹 Latency tracking
    latency = time.time() - start
    LATENCY.observe(latency)

    # 🔹 Request count
    REQUEST_COUNT.inc()

    return result


# ---------------- INVENTORY ----------------
@app.post("/inventory/reorder")
def inventory(req: InventoryRequest):

    start = time.time()

    logging.info("📦 Inventory reorder called")

    log = {
        "event": "inventory_reorder",
        "sku_id": req.sku_id,
        "current_stock": req.current_stock,
        "timestamp": time.time()
    }
    print(json.dumps(log))

    result = reorder_suggestion(req)

    latency = time.time() - start
    LATENCY.observe(latency)
    REQUEST_COUNT.inc()

    return result