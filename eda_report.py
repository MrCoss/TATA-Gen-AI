import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_excel(r'D:\Projects\TATA GENAI\data\Delinquency_prediction_dataset.xlsx')

# 1. Dataset Overview
print("📌 Dataset Shape:", df.shape)
print("📌 Column Names:\n", df.columns.tolist())
print("📌 Data Types:\n", df.dtypes)
print("📌 First 5 Rows:\n", df.head())

# 2. Missing Data Analysis
print("\n📌 Missing Values:\n", df.isnull().sum())
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Missing Data Heatmap')
plt.show()

# 3. Summary Statistics
print("\n📌 Summary Statistics (Numerical):\n", df.describe())
print("\n📌 Summary Statistics (Categorical):\n", df.describe(include=['object']))

# 4. Correlation Matrix
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# 5. Value Counts for Target (if applicable)
if 'target' in df.columns:
    print("\n📌 Target Value Distribution:\n", df['target'].value_counts())
    sns.countplot(data=df, x='target')
    plt.title("Target Class Distribution")
    plt.show()

# 6. Distribution of Numerical Features
num_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[num_cols].hist(bins=15, figsize=(15, 10))
plt.suptitle("Numerical Feature Distributions")
plt.show()
