import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    print("Data Loaded:", df.shape)
    return df