def export_high_risk(rfm):
    print("📤 Exporting high-risk customers...")

    high_risk = rfm[
        (rfm['recency'] > rfm['recency'].quantile(0.7)) &
        (rfm['frequency'] < rfm['frequency'].quantile(0.3))
    ]

    high_risk['action'] = "SEND_DISCOUNT"

    high_risk.to_csv("reports/high_churn_customers.csv", index=False)