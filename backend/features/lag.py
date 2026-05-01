def create_lag_features(df):
    df['lag_1'] = df['TotalPrice'].shift(1)
    df['lag_7'] = df['TotalPrice'].shift(7)
    df['lag_14'] = df['TotalPrice'].shift(14)

    return df