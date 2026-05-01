def segment_profile(rfm):
    print("📊 Creating segment profiles...")

    profile = rfm.groupby('cluster').agg({
        'recency': 'mean',
        'frequency': 'mean',
        'monetary': 'mean',
        'customer_id': 'count'
    }).rename(columns={'customer_id': 'num_customers'})

    print(profile)

    profile.to_csv("reports/segment_profile.csv")

    return profile