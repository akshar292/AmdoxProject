import pandas as pd
import sweetviz as sv

df = pd.read_csv("data/processed/feature_store.csv")

report = sv.analyze(df)
report.show_html("report.html")

print("EDA Report Generated ✅")