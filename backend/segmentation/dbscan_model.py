from sklearn.cluster import DBSCAN

def run_dbscan(X, rfm):
    print("🧪 Running DBSCAN...")

    model = DBSCAN(eps=0.8, min_samples=5)
    rfm['dbscan_cluster'] = model.fit_predict(X)

    return rfm