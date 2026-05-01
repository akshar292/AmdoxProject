import pandas as pd
from ydata_profiling import ProfileReport

def generate_report():
    df = pd.read_csv("data/processed/feature_data.csv")

    profile = ProfileReport(df, title="NeuralRetail Report")

    profile.to_file("data/processed/report.html")

    print("Report generated ✅")