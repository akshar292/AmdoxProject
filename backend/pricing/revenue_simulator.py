def simulate_revenue(price, elasticity, base_demand):

    print("💰 Running Revenue Simulation...")

    new_demand = base_demand * (price / 100) ** elasticity
    revenue = price * new_demand

    print(f"Price: {price}")
    print(f"Estimated Demand: {new_demand:.2f}")
    print(f"Revenue: {revenue:.2f}")

    return new_demand, revenue