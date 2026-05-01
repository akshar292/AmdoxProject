import pandas as pd
import numpy as np

df = pd.read_csv("data/processed/time_series.csv")

# Fake price (for demo)
np.random.seed(42)
df['price'] = np.random.randint(80, 150, size=len(df))

# Demand = count
df['demand'] = df['count']

# Promotion flag
df['promotion'] = np.random.choice([0, 1], size=len(df))

df[['price', 'demand', 'promotion']].to_csv(
    "data/processed/pricing_data.csv",
    index=False
)

print("✅ pricing_data.csv created")