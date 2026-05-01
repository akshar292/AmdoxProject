def create_rolling_features(df):
    df = df.sort_values('InvoiceDate')

    df['rolling_mean_7'] = df['TotalPrice'].rolling(7).mean()
    df['rolling_std_7'] = df['TotalPrice'].rolling(7).std()

    return df