import pandas as pd

def prepare_time_series():
    df = pd.read_csv("data/processed/feature_store.csv")

    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # count events per day
    ts = df.groupby(df['timestamp'].dt.date).size().reset_index(name='count')

    ts.columns = ['date', 'count']

    ts.to_csv("data/processed/time_series.csv", index=False)

    print("Time series data ready ✅")

if __name__ == "__main__":
    prepare_time_series()