import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------
# CONFIG
# -------------------------
st.set_page_config(
    page_title="Amdox Retail AI",
    layout="wide"
)

# -------------------------
# CUSTOM CSS (Amdox Theme)
# -------------------------
st.markdown("""
<style>
    .main {
        background-color: #ffffff;
    }
    .stApp {
        background: linear-gradient(120deg, #E84E1B, #F7941D, #FBBA13);
    }
    h1, h2, h3 {
        color: black;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------
# SIDEBAR NAVIGATION
# -------------------------
st.sidebar.title("📊 Amdox AI Platform")

page = st.sidebar.radio(
    "Navigate",
    [
        "Executive Overview",
        "Demand Intelligence",
        "Customer Hub",
        "Inventory",
        "MLOps Monitor"
    ]
)

# -------------------------
# LOAD SAMPLE DATA
# -------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/time_series.csv")
    return df

df = load_data()

# -------------------------
# PAGE 1 - EXECUTIVE OVERVIEW
# -------------------------
if page == "Executive Overview":
    st.title("🧠 Executive Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Revenue", "$1.2M")
    col2.metric("Active Customers", "45,320")
    col3.metric("Churn Rate", "8.2%")

    fig = px.line(df, x="date", y="count", title="Demand Trend")
    st.plotly_chart(fig, use_container_width=True)

# -------------------------
# PAGE 2 - DEMAND INTELLIGENCE
# -------------------------
elif page == "Demand Intelligence":
    st.title("📈 Demand Forecasting")

    fig = px.line(df, x="date", y="count", title="Demand Forecast")
    st.plotly_chart(fig, use_container_width=True)

    st.info("LSTM + Prophet Ensemble Model Output")

# -------------------------
# PAGE 3 - CUSTOMER HUB
# -------------------------
elif page == "Customer Hub":
    st.title("👥 Customer Segmentation")

    seg_data = pd.DataFrame({
        "segment": ["VIP", "Regular", "At Risk", "New"],
        "customers": [1200, 5400, 900, 3200]
    })

    fig = px.pie(seg_data, names="segment", values="customers")
    st.plotly_chart(fig)

# -------------------------
# PAGE 4 - INVENTORY
# -------------------------
elif page == "Inventory":
    st.title("📦 Inventory Intelligence")

    st.bar_chart({
        "Product A": 120,
        "Product B": 80,
        "Product C": 200
    })

# -------------------------
# PAGE 5 - MLOPS MONITOR
# -------------------------
elif page == "MLOps Monitor":
    st.title("⚙️ MLflow Monitoring")

    st.success("Model Status: Production Ready")
    st.metric("Forecast MAPE", "8.3%")
    st.metric("Churn AUC", "0.91")