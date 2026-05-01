import numpy as np
import statsmodels.api as sm

def run_elasticity_model(df):

    print("📊 Running Price Elasticity Model...")

    df = df.copy()

    df['log_price'] = np.log(df['price'])
    df['log_demand'] = np.log(df['demand'])

    X = df[['log_price', 'promotion']]
    X = sm.add_constant(X)

    y = df['log_demand']

    model = sm.OLS(y, X).fit()

    print(model.summary())

    elasticity = model.params['log_price']
    print(f"📉 Price Elasticity: {elasticity:.4f}")

    return model, elasticity