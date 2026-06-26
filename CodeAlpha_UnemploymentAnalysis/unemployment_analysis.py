import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("Unemployment in India.csv")

# Remove extra spaces from column names
data.columns = data.columns.str.strip()

# Display first 5 rows
print(data.head())

# Dataset information
print("\nDataset Information:")
print(data.info())

# Missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Basic statistics
print("\nBasic Statistics:")
print(data.describe())

# Histogram
plt.figure(figsize=(8,5))
plt.hist(data["Estimated Unemployment Rate (%)"], bins=10)
plt.title("Distribution of Unemployment Rate")
plt.xlabel("Estimated Unemployment Rate (%)")
plt.ylabel("Number of Records")
plt.show()

# Average unemployment rate by region
avg = data.groupby("Region")["Estimated Unemployment Rate (%)"].mean()

plt.figure(figsize=(12,6))
avg.plot(kind="bar")

plt.title("Average Unemployment Rate by Region")
plt.xlabel("Region")
plt.ylabel("Average Unemployment Rate (%)")

plt.xticks(rotation=90)
plt.tight_layout()

plt.show()

# Top 5 regions
top5 = avg.sort_values(ascending=False).head(5)

plt.figure(figsize=(7,7))
plt.pie(top5, labels=top5.index, autopct="%1.1f%%")

plt.title("Top 5 Regions by Average Unemployment Rate")

plt.show()