def validate_data(df):
    assert df.shape[0] > 0, "Empty dataset!"
    assert df.isnull().sum().sum() == 0, "Null values found!"
    print("Data validation passed ✅")