import shap
import pandas as pd
import matplotlib.pyplot as plt
import os

from .prepare_data import load_churn_data
from .train_xgb import train_xgb


def run_shap_explain():

    print("🔍 Running SHAP Explainability...")

    # Load data
    X, y = load_churn_data()

    # Train model
    model, X_test, y_test = train_xgb(X, y)

    # SHAP explainer
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_test)

    # Create output folder
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)

    # 🔹 Global Feature Importance
    print("📊 Saving SHAP summary plot...")
    shap.summary_plot(shap_values, X_test, show=False)
    plt.savefig(f"{output_dir}/shap_summary.png")
    plt.clf()

    # 🔹 Bar Plot
    shap.summary_plot(shap_values, X_test, plot_type="bar", show=False)
    plt.savefig(f"{output_dir}/shap_bar.png")
    plt.clf()

    # 🔹 Local Explanation (single example)
    print("📌 Saving SHAP waterfall plot...")
    shap.plots._waterfall.waterfall_legacy(
        explainer.expected_value[0],
        shap_values[0][0],
        X_test.iloc[0]
    )
    plt.savefig(f"{output_dir}/shap_waterfall.png")
    plt.clf()

    print("✅ SHAP analysis completed. Check /outputs folder.")


if __name__ == "__main__":
    run_shap_explain()