def run_checks(df):
    assert df.shape[0] > 0, "Empty dataset!"

    assert 'timestamp' in df.columns, "Missing timestamp!"

    assert df.isnull().sum().sum() == 0, "Null values found!"

    print("Data quality checks passed ✅")