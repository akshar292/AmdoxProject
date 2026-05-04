import streamlit as st
import pandas as pd
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
st.title("📦 Inventory Optimization")

# ---------- KPI ----------
i1, i2, i3 = st.columns(3)
i1.metric("Stock Level", "2300")
i2.metric("Low Stock", "12")
i3.metric("Reorder", "5")

# ---------- DATA ----------
data = pd.DataFrame({
    "Product": ["A", "B", "C", "D"],
    "Stock": [120, 80, 200, 60]
})

# ---------- CHART ----------
card("<h3>📊 Inventory Levels</h3>")

fig = px.bar(data, x="Product", y="Stock", color="Stock")
fig.update_layout(template="plotly_dark")

st.plotly_chart(fig, use_container_width=True)

# ---------- ALERT ----------
low = data[data["Stock"] < 100]

if not low.empty:
    st.warning("⚠️ Low Stock Detected")
    st.dataframe(low)

# ---------- AI ----------
card("<h3>🤖 Suggestion</h3><p>Reorder Product B & D</p>")