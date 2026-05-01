import pandas as pd
from statsmodels.tsa.stattools import adfuller

df = pd.read_csv("data/processed/time_series.csv")

result = adfuller(df['count'])

print("ADF Statistic:", result[0])
print("p-value:", result[1])

if result[1] < 0.05:
    print("Data is stationary ✅")
else:
    print("Data is NOT stationary ❌")