import pandas as pd

def create_date_features(df):
    # convert timestamp (milliseconds → datetime)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    df['day_of_week'] = df['timestamp'].dt.dayofweek
    df['week_of_year'] = df['timestamp'].dt.isocalendar().week
    df['month'] = df['timestamp'].dt.month

    return df