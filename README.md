# NeuralRetail AI Platform

End-to-end retail intelligence system with **Demand Forecasting**, **Customer Intelligence (Churn Risk)**, and **Inventory Optimization**.
Includes **FastAPI backend**, **Streamlit dashboard**, and **Prometheus metrics**.

---

## 🚀 Features

* 📈 **Demand Forecasting**

  * Real-time predictions via API
  * What-if simulation (price, promotion, season)
* 👥 **Customer Intelligence**

  * Churn risk scoring
  * Customer 360 view
  * Retention action suggestions
* 📦 **Inventory Optimization**

  * Stock monitoring dashboard
  * Low-stock alerts
  * Reorder recommendations
* ⚙️ **MLOps Ready**

  * `/metrics` endpoint (Prometheus)
  * Structured logging
  * API authentication

---

## 🏗️ Architecture

```text
User (Streamlit UI)
        ↓
FastAPI Backend (Inference API)
        ↓
ML Models (Demand / Churn)
        ↓
Metrics (Prometheus) + Logs
```

---

## 🧪 API Endpoints

* `GET /health` → health check
* `GET /metrics` → Prometheus metrics
* `POST /predict/demand` → demand prediction
* `POST /inventory/reorder` → reorder suggestion

---

## ⚙️ Local Setup

### 1. Clone repo

```bash
git clone https://github.com/akshar292/AmdoxProject.git
cd AmdoxProject
```

### 2. Create environment

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run backend

```bash
python -m uvicorn backend.api.main:app --reload
```

### 4. Run dashboard

```bash
streamlit run dashboard/app.py
```

---

## 📊 Demo

* Open: http://127.0.0.1:8000/docs
* Test `/predict/demand` with API key

---

## 📁 Project Structure

```
backend/
  api/
dashboard/
  pages/
models/
data/
```

---

## 📦 Tech Stack

* FastAPI
* Streamlit
* Plotly
* Scikit-learn / ML models
* Prometheus metrics

---

## 👤 Author

Akshar Bhavsar
