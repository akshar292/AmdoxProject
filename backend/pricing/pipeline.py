from backend.pricing.prepare_data import load_pricing_data
from backend.pricing.elasticity_model import run_elasticity_model
# from backend.pricing.causal_model import run_causal_inference   ❌ optional
from backend.pricing.uplift_model import calculate_promotion_lift
from backend.pricing.revenue_simulator import simulate_revenue


def run_pricing_pipeline():

    print("🚀 Running Pricing Intelligence Pipeline...")

    df = load_pricing_data()

    # Elasticity
    model, elasticity = run_elasticity_model(df)

    # 🔹 Try causal inference safely
    try:
        from backend.pricing.causal_model import run_causal_inference
        causal_effect = run_causal_inference(df)
    except Exception as e:
        print("⚠️ Skipping causal inference:", e)

    # Promotion lift
    lift = calculate_promotion_lift(df)

    # Revenue simulation
    simulate_revenue(price=120, elasticity=elasticity, base_demand=1000)

    print("✅ Pricing Intelligence Completed!")


if __name__ == "__main__":
    run_pricing_pipeline()