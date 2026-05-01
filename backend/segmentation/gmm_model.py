from sklearn.mixture import GaussianMixture

def run_gmm(X, rfm, k):
    print("📈 Running GMM...")

    model = GaussianMixture(n_components=k, random_state=42)
    rfm['gmm_cluster'] = model.fit_predict(X)

    return rfm