import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution(df):
    df.hist(figsize=(10, 6))
    plt.show()

def correlation_heatmap(df):
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, cmap='coolwarm')
    plt.show()