import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/time_series.csv")

df['date'] = pd.to_datetime(df['date'])

plt.plot(df['date'], df['count'])
plt.title("Event Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Event Count")
plt.show()