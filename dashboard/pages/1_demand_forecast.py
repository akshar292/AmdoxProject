import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import io

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.title("📈 Demand Forecast Explorer")

# ---------------------------
# LOAD DATA (replace with ML output later)
# ---------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/time_series.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df

df = load_data()

# ---------------------------
# SIDEBAR FILTERS
# ---------------------------
st.sidebar.header("🔍 Filters")

start_date = st.sidebar.date_input("Start Date", df["date"].min())
end_date = st.sidebar.date_input("End Date", df["date"].max())

sku = st.sidebar.text_input("Search SKU", "SKU-101")

filtered = df[(df["date"] >= pd.to_datetime(start_date)) &
              (df["date"] <= pd.to_datetime(end_date))]

# ---------------------------
# FAKE FORECAST (replace with LSTM output)
# ---------------------------
filtered["forecast"] = filtered["count"] * (1 + np.random.normal(0, 0.05, len(filtered)))
filtered["upper"] = filtered["forecast"] * 1.1
filtered["lower"] = filtered["forecast"] * 0.9

# ---------------------------
# FORECAST CHART
# ---------------------------
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=filtered["date"],
    y=filtered["count"],
    mode="lines",
    name="Actual"
))

fig.add_trace(go.Scatter(
    x=filtered["date"],
    y=filtered["forecast"],
    mode="lines",
    name="Forecast"
))

# Confidence band
fig.add_trace(go.Scatter(
    x=filtered["date"],
    y=filtered["upper"],
    fill=None,
    mode="lines",
    line=dict(color="lightgray"),
    showlegend=False
))

fig.add_trace(go.Scatter(
    x=filtered["date"],
    y=filtered["lower"],
    fill="tonexty",
    mode="lines",
    line=dict(color="lightgray"),
    name="Confidence Interval"
))

st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# WHAT-IF SIMULATOR
# ---------------------------
st.subheader("⚙️ What-If Simulator")

price_factor = st.slider("Price Impact", 0.5, 1.5, 1.0)
promo_flag = st.selectbox("Promotion", [0, 1])
weather_factor = st.slider("Weather Impact", 0.8, 1.2, 1.0)

simulated = filtered.copy()
simulated["what_if_demand"] = (
    simulated["forecast"] *
    price_factor *
    weather_factor *
    (1.2 if promo_flag == 1 else 1.0)
)

st.line_chart(simulated[["forecast", "what_if_demand"]])

# ---------------------------
# MAPE LEADERBOARD
# ---------------------------
st.subheader("🏆 Forecast Accuracy Leaderboard")

leaderboard = pd.DataFrame({
    "SKU": ["SKU-101", "SKU-102", "SKU-103"],
    "Category": ["A", "B", "A"],
    "MAPE": [6.2, 8.9, 11.3]
}).sort_values("MAPE")

st.dataframe(leaderboard)

# ---------------------------
# EXPORTS
# ---------------------------

st.subheader("📦 Export Tools")

# Excel export
excel_buffer = io.BytesIO()
leaderboard.to_excel(excel_buffer, index=False)
excel_buffer.seek(0)

st.download_button(
    "⬇️ Download Forecast Excel",
    excel_buffer,
    file_name="forecast_report.xlsx"
)

# PNG export (chart)
fig.write_image("forecast.png")

st.success("Chart saved as PNG (forecast.png)")