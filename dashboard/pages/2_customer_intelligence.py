import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import io

st.title("👥 Customer Intelligence & Churn Module")

# -------------------------
# LOAD DATA (replace with model output later)
# -------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/feature_store.csv")
    return df

df = load_data()

# Fake churn score (replace with XGBoost output)
df["churn_risk"] = np.random.rand(len(df))
df["risk_decile"] = pd.qcut(df["churn_risk"], 10, labels=False)

# -------------------------
# CHURN HEATMAP
# -------------------------
st.subheader("🔥 Churn Risk Heatmap (Segment × Risk)")

heatmap = pd.crosstab(df["risk_decile"], df["visitorid"] % 5)

fig = px.imshow(
    heatmap,
    labels=dict(x="Segment", y="Risk Decile", color="Count"),
    title="Churn Risk Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------
# CUSTOMER 360 VIEW
# -------------------------
st.subheader("🧠 Customer 360 View")

customer_id = st.selectbox("Select Customer", df["visitorid"].unique())

cust = df[df["visitorid"] == customer_id].head(1)

st.metric("Churn Risk", f"{cust['churn_risk'].values[0]:.2f}")

st.write("📦 Customer Data")
st.dataframe(cust)

# -------------------------
# RETENTION ACTION ENGINE
# -------------------------
st.subheader("📢 Retention Action Board")

def action_plan(risk):
    if risk > 0.7:
        return "🚨 High Risk: Offer discount + call support team"
    elif risk > 0.4:
        return "⚠️ Medium Risk: Send personalized email campaign"
    else:
        return "✅ Low Risk: Standard engagement"

df["action"] = df["churn_risk"].apply(action_plan)

st.dataframe(df[["visitorid", "churn_risk", "action"]].head(10))

# -------------------------
# SEGMENT COMPARISON (RFM STYLE)
# -------------------------
st.subheader("📊 Segment Comparison Radar")

rfm_demo = pd.DataFrame({
    "segment": ["VIP", "Regular", "At Risk"],
    "recency": [80, 50, 20],
    "frequency": [90, 40, 20],
    "monetary": [95, 60, 25]
})

fig = px.line_polar(
    rfm_demo,
    r="recency",
    theta="segment",
    line_close=True
)

st.plotly_chart(fig)

# -------------------------
# CAMPAIGN EXPORT
# -------------------------
st.subheader("📦 Campaign Builder")

selected_risk = st.slider("Select Risk Threshold", 0.0, 1.0, 0.6)

campaign_df = df[df["churn_risk"] > selected_risk]

st.write(f"Selected Customers: {len(campaign_df)}")

buffer = io.StringIO()
campaign_df.to_csv(buffer, index=False)

st.download_button(
    "⬇️ Download CRM Campaign CSV",
    buffer.getvalue(),
    file_name="crm_campaign.csv",
    mime="text/csv"
)