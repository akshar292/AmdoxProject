import pandas as pd
from prophet import Prophet

def run_forecast():
    df = pd.read_csv("data/processed/time_series.csv")

    df.columns = ['ds', 'y']   # Prophet format

    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=30)

    forecast = model.predict(future)

    model.plot(forecast)

    print("Forecast completed ✅")

if __name__ == "__main__":
    run_forecast()