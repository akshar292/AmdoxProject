import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide")

# ---------- GLOBAL CSS ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: #e2e8f0;
}
.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 16px;
    margin-bottom: 20px;
}
h1,h2,h3 { color: white; }
</style>
""", unsafe_allow_html=True)

def card(content):
    st.markdown(f"<div class='card'>{content}</div>", unsafe_allow_html=True)

# ---------- TITLE ----------
st.title("📈 Demand Forecast")

# ---------- DATA ----------
df = pd.DataFrame({
    "date": pd.date_range(start="2024-01-01", periods=30),
    "count": np.random.randint(80, 200, 30)
})

# ---------- FILTER ----------
col1, col2 = st.columns(2)
start = col1.date_input("Start Date", df["date"].min())
end = col2.date_input("End Date", df["date"].max())

df = df[(df["date"] >= pd.to_datetime(start)) & (df["date"] <= pd.to_datetime(end))]

# ---------- KPI ----------
k1, k2, k3 = st.columns(3)
k1.metric("Avg Demand", int(df["count"].mean()))
k2.metric("Peak Demand", int(df["count"].max()))
k3.metric("Growth", "+8%")

# ---------- CHART ----------
card("<h3>📊 Forecast Trend</h3>")

fig = px.area(df, x="date", y="count")
fig.update_layout(template="plotly_dark")

st.plotly_chart(fig, use_container_width=True)

# ---------- WHAT IF ----------
st.subheader("⚙️ What-If Simulator")

price = st.slider("Price Impact", 0.5, 1.5, 1.0)
promo = st.selectbox("Promotion", [0, 1])

df["simulation"] = df["count"] * price * (1.2 if promo else 1)

st.line_chart(df[["count", "simulation"]])