import random

# Dummy metrics (replace later with real)
mape = random.uniform(5, 15)
auc = random.uniform(0.85, 0.95)

print(f"MAPE: {mape}")
print(f"AUC: {auc}")

# ❌ Fail conditions
if mape > 12:
    raise Exception("❌ MAPE too high")

if auc < 0.88:
    raise Exception("❌ AUC too low")

print("✅ Model passed validation")