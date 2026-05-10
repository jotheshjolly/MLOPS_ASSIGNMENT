import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def load_and_clean_data(filepath):
    cols = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
            'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']
    df = pd.read_csv(filepath, names=cols, na_values='?')
    
    # Handle missing values
    df = df.fillna(df.median())
    
    # Binarize target: 0 stays 0, >0 becomes 1
    df['target'] = df['target'].apply(lambda x: 1 if x > 0 else 0)
    return df

def generate_eda_plots(df):
    # Correlation Heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title("Feature Correlation Heatmap")
    plt.savefig("correlation_heatmap.png")
    
    # Class Balance Plot
    plt.figure(figsize=(6, 4))
    sns.countplot(x='target', data=df)
    plt.title("Class Balance (0: No Disease, 1: Disease)")
    plt.savefig("class_balance.png")

if __name__ == "__main__":
    data = load_and_clean_data('./data/processed.cleveland.data')
    generate_eda_plots(data)