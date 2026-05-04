import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide")

# ---------- CSS ----------
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
st.title("👥 Customer Intelligence")

# ---------- DATA ----------
df = pd.DataFrame({
    "customer": range(1, 100),
    "churn_risk": np.random.rand(99)
})

# ---------- KPI ----------
c1, c2, c3 = st.columns(3)
c1.metric("Customers", "45K")
c2.metric("VIP", "1.2K")
c3.metric("Churn Risk", "8%")

# ---------- SEGMENT ----------
segments = pd.DataFrame({
    "segment": ["VIP", "Regular", "At Risk", "New"],
    "value": [1200, 5400, 900, 3200]
})

card("<h3>📊 Customer Segments</h3>")

fig = px.pie(segments, names="segment", values="value")
fig.update_layout(template="plotly_dark")

st.plotly_chart(fig, use_container_width=True)

# ---------- CUSTOMER VIEW ----------
st.subheader("🧠 Customer 360 View")

cid = st.selectbox("Select Customer", df["customer"])

risk = df[df["customer"] == cid]["churn_risk"].values[0]

st.metric("Churn Risk", f"{risk:.2f}")

# ---------- ACTION ----------
def action(r):
    if r > 0.7:
        return "🚨 High Risk"
    elif r > 0.4:
        return "⚠️ Medium Risk"
    else:
        return "✅ Safe"

card(f"<h3>🤖 Action</h3><p>{action(risk)}</p>")