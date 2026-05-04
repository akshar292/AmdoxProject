import streamlit as st
import pandas as pd
import plotly.express as px
import requests

# -------------------------
# CONFIG
# -------------------------
st.set_page_config(
    page_title="Amdox Retail AI",
    layout="wide",
    initial_sidebar_state="expanded"
)

API_URL = "http://127.0.0.1:8000"
API_KEY = "12345"

# -------------------------
# PREMIUM CSS
# -------------------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: #e2e8f0;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617, #0f172a);
}
[data-testid="stSidebar"] * {
    color: white !important;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(12px);
    border-radius: 18px;
    padding: 20px;
    margin-bottom: 20px;
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg,#f97316,#fb923c);
    color: white;
    border-radius: 10px;
    font-weight: bold;
}

/* Headings */
h1, h2, h3 {
    color: #f8fafc;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.markdown("""
<h2>🚀 Amdox AI</h2>
<p style='opacity:0.6;'>Retail Intelligence Platform</p>
""", unsafe_allow_html=True)

page = st.sidebar.radio(
    "Navigate",
    ["Dashboard", "Demand Forecast", "Customer Intelligence", "Inventory Optimization"]
)

# -------------------------
# SAMPLE DATA
# -------------------------
@st.cache_data
def load_data():
    return pd.DataFrame({
        "date": pd.date_range(start="2024-01-01", periods=30),
        "count": [100 + i*2 for i in range(30)]
    })

df = load_data()

# -------------------------
# DASHBOARD
# -------------------------
if page == "Dashboard":

    st.title("🧠 Executive Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.markdown("""
    <div class="card">
    <h4>Revenue</h4>
    <h1>$1.2M</h1>
    <span style="color:#22c55e">+12%</span>
    </div>
    """, unsafe_allow_html=True)

    col2.markdown("""
    <div class="card">
    <h4>Customers</h4>
    <h1>45K</h1>
    <span style="color:#22c55e">+5%</span>
    </div>
    """, unsafe_allow_html=True)

    col3.markdown("""
    <div class="card">
    <h4>Churn Rate</h4>
    <h1>8.2%</h1>
    <span style="color:#ef4444">-1.2%</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    fig = px.line(df, x="date", y="count")
    fig.update_layout(template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# DEMAND FORECAST
# -------------------------
elif page == "Demand Forecast":

    st.title("📈 Demand Forecast")

    col1, col2, col3 = st.columns(3)

    price = col1.slider("Price", 50, 500, 100)
    promo = col2.selectbox("Promotion", [0, 1])
    season = col3.slider("Season", 1, 12, 5)

    if st.button("🚀 Predict Demand"):

        with st.spinner("Predicting... 🤖"):
            try:
                res = requests.post(
                    f"{API_URL}/predict/demand",
                    json={
                        "sku_id": 101,
                        "price": price,
                        "promo_flag": promo,
                        "season": season
                    },
                    headers={"x-api-key": API_KEY}
                )

                if res.status_code == 200:
                    result = res.json()

                    st.markdown(f"""
                    <div class="card">
                    <h3>🔥 Predicted Demand</h3>
                    <h1>{result['predicted_demand']}</h1>
                    </div>
                    """, unsafe_allow_html=True)

                else:
                    st.error("API Error")

            except Exception as e:
                st.error(f"Error: {e}")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    fig = px.area(df, x="date", y="count")
    fig.update_layout(template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# CUSTOMER INTELLIGENCE
# -------------------------
elif page == "Customer Intelligence":

    st.title("👥 Customer Intelligence")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Customers", "45K", "+5%")
    col2.metric("VIP Users", "1.2K", "+10%")
    col3.metric("Churn Risk", "900", "-3%")

    data = pd.DataFrame({
        "segment": ["VIP", "Regular", "At Risk", "New"],
        "value": [1200, 5400, 900, 3200]
    })

    st.markdown('<div class="card">', unsafe_allow_html=True)
    fig = px.pie(data, names="segment", values="value")
    fig.update_layout(template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>🤖 AI Insight</h3>
    <p>VIP users are growing. Focus retention on at-risk customers.</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------
# INVENTORY OPTIMIZATION
# -------------------------
elif page == "Inventory Optimization":

    st.title("📦 Inventory Optimization")

    col1, col2, col3 = st.columns(3)

    col1.metric("Stock Level", "2300 units")
    col2.metric("Low Stock Items", "12")
    col3.metric("Reorder Needed", "5")

    data = pd.DataFrame({
        "Product": ["Product A", "Product B", "Product C"],
        "Stock": [120, 80, 200]
    })

    st.bar_chart(data.set_index("Product"))

    st.success("Reorder Product B to avoid stockout")