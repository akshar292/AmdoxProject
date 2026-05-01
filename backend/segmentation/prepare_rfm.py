import pandas as pd

def create_rfm(df):

    print("🔥 Creating RFM features...")

    df = df.rename(columns={
        "visitorid": "customer_id",
        "timestamp": "date"
    })

    df['date'] = pd.to_datetime(df['date'])

    df['amount'] = df['transactionid'].apply(lambda x: 1 if x != 0 else 0)

    snapshot_date = df['date'].max()

    rfm = df.groupby('customer_id').agg({
        'date': lambda x: (snapshot_date - x.max()).days,
        'customer_id': 'count',
        'amount': 'sum'
    })

    rfm.rename(columns={
        'date': 'recency',
        'customer_id': 'frequency',
        'amount': 'monetary'
    }, inplace=True)

    rfm = rfm.reset_index()

    print("✅ RFM Created Successfully")
    print(rfm.head())

    return rfm