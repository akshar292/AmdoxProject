def calculate_promotion_lift(df):

    print("📈 Calculating Promotion Lift...")

    before = df[df['promotion'] == 0]['demand'].mean()
    after = df[df['promotion'] == 1]['demand'].mean()

    lift = (after - before) / before

    print(f"🚀 Promotion Lift: {lift:.4f}")

    return lift