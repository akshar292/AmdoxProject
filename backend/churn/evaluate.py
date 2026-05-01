from sklearn.metrics import classification_report, roc_auc_score

def evaluate_model(model, X_test, y_test):

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)

    print("\n📊 Classification Report:\n")
    print(classification_report(y_test, y_pred))

    # ✅ FIX: multi-class AUC
    auc = roc_auc_score(y_test, y_prob, multi_class='ovr')

    print("AUC-ROC:", auc)