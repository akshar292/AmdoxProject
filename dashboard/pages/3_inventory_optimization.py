import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import io

st.title("📦 Inventory Optimization Module")

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/processed/feature_store.csv")

df = load_data()

# -----------------------------
# MOCK FEATURES
# -----------------------------
np.random.seed(42)

df["stock"] = np.random.randint(0, 500, len(df))
df["demand"] = np.random.randint(10, 100, len(df))
df["lead_time_days"] = np.random.randint(2, 15, len(df))
df["holding_cost"] = np.random.uniform(1, 5, len(df))

# -----------------------------
# ABC-XYZ CLASSIFICATION
# -----------------------------
def classify(row):
    if row["demand"] > 80:
        return "A-X"
    elif row["demand"] > 50:
        return "B-Y"
    else:
        return "C-Z"

df["abc_xyz"] = df.apply(classify, axis=1)

# -----------------------------
# STOCKOUT RISK
# -----------------------------
df["stockout_risk"] = df["demand"] / (df["stock"] + 1)

df["dead_stock"] = df["stock"] > 300

# -----------------------------
# SCORECARD
# -----------------------------
st.subheader("📊 Inventory Health Scorecard")

fig = px.scatter(
    df,
    x="stock",
    y="demand",
    color="abc_xyz"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# EOQ
# -----------------------------
st.subheader("⚙️ EOQ Calculator")

ordering_cost = st.number_input("Ordering Cost", value=50)
holding_cost = st.number_input("Holding Cost", value=2)
annual_demand = st.number_input("Annual Demand", value=1000)

eoq = np.sqrt((2 * annual_demand * ordering_cost) / holding_cost)
safety_stock = df["demand"].mean() * 1.2

st.metric("EOQ", f"{eoq:.0f}")
st.metric("Safety Stock", f"{safety_stock:.0f}")

# -----------------------------
# REORDER ALERT (SAFE)
# -----------------------------
st.subheader("🚨 Reorder Alerts")

reorder = df[df["stock"] < df["demand"] * 1.5]

if len(reorder) > 0:
    reorder = reorder.copy()
    reorder["urgency_score"] = reorder["stockout_risk"] * 100
    st.dataframe(reorder[["stock", "demand", "urgency_score"]].head(10))
else:
    st.info("No reorder alerts")

# -----------------------------
# OVERSTOCK
# -----------------------------
st.subheader("📉 Overstock Risk Panel")

overstock = df[df["stock"] > 300]

if len(overstock) > 0:
    st.dataframe(overstock[["stock", "abc_xyz"]].head(10))
else:
    st.info("No overstock items")

# -----------------------------
# LEAD TIME
# -----------------------------
st.subheader("🚚 Supplier Lead Time Analysis")

fig2 = px.histogram(df, x="lead_time_days")
st.plotly_chart(fig2)

# -----------------------------
# EXPORT
# -----------------------------
st.subheader("📦 Export Inventory Report")

buffer = io.StringIO()
df.to_csv(buffer, index=False)

st.download_button(
    "⬇️ Download CSV",
    buffer.getvalue(),
    file_name="inventory_report.csv",
    mime="text/csv"
)