from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score

def scale_features(rfm):
    scaler = StandardScaler()
    X = scaler.fit_transform(rfm[['recency', 'frequency', 'monetary']])
    return X


def find_best_k(X):
    print("🔍 Finding best K...")

    results = []

    for k in range(6, 11):
        model = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = model.fit_predict(X)

        sil = silhouette_score(X, labels)
        db = davies_bouldin_score(X, labels)

        print(f"K={k} | Silhouette={sil:.3f} | DB={db:.3f}")
        results.append((k, db))

    best_k = sorted(results, key=lambda x: x[1])[0][0]

    print(f"✅ Best K: {best_k}")
    return best_k


def run_kmeans(X, rfm, k):
    print("📊 Running KMeans...")
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    rfm['cluster'] = model.fit_predict(X)
    return rfm