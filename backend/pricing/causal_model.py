from dowhy import CausalModel

def run_causal_inference(df):

    print("🔬 Running Causal Inference...")

    model = CausalModel(
        data=df,
        treatment="price",
        outcome="demand",
        common_causes=["promotion"]
    )

    identified = model.identify_effect()

    estimate = model.estimate_effect(
        identified,
        method_name="backdoor.linear_regression"
    )

    print("📌 Causal Effect:", estimate.value)

    return estimate.value