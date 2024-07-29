import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from GitHub raw URL
url = 'https://raw.githubusercontent.com/jaivrma/Rossmann-Store-Sales/main/train.csv'
dataframe = pd.read_csv(url, low_memory=False)

# Print column names to inspect them
print("Column Names:", dataframe.columns)

# Convert 'Date' to datetime type
dataframe['Date'] = pd.to_datetime(dataframe['Date'])

# Check for missing values
print("Missing Values:", dataframe.isnull().sum())

# Fill missing values if necessary (e.g., 'Open' column)
dataframe['Open'].fillna(1, inplace=True)

# Display data types and basic statistics
print("Data Types:", dataframe.dtypes)
print("Basic Statistics:", dataframe.describe())

# Set the style of the plots
sns.set_style("whitegrid")

# Sales distribution by day of the week
plt.figure(figsize=(10, 6))
sns.boxplot(x='DayOfWeek', y='Sales', data=dataframe, palette='viridis')
plt.title('Sales Distribution by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Sales')
plt.show()

# Conclusion: Sales vary across different days of the week, with some days showing higher sales. This indicates customer shopping patterns and store performance variations.

# Sales over time
plt.figure(figsize=(12, 6))
dataframe.groupby('Date')['Sales'].sum().plot(color='purple', linewidth=2, marker='o')
plt.title('Total Sales over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()

# Conclusion: The total sales over time show seasonal trends and periodic peaks, indicating the importance of seasonal promotions and inventory planning.

# Effect of promotions on sales
plt.figure(figsize=(10, 6))
sns.boxplot(x='Promo', y='Sales', data=dataframe, palette='coolwarm')
plt.title('Effect of Promotions on Sales')
plt.xlabel('Promo')
plt.ylabel('Sales')
plt.show()

# Conclusion: Promotions significantly boost sales, showcasing the effectiveness of promotional strategies in increasing revenue.

# Sales distribution on State and School holidays
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

sns.boxplot(x='StateHoliday', y='Sales', data=dataframe, palette='viridis', ax=axes[0])
axes[0].set_title('Sales Distribution on State Holidays')
axes[0].set_xlabel('State Holiday')
axes[0].set_ylabel('Sales')

sns.boxplot(x='SchoolHoliday', y='Sales', data=dataframe, palette='viridis', ax=axes[1])
axes[1].set_title('Sales Distribution on School Holidays')
axes[1].set_xlabel('School Holiday')
axes[1].set_ylabel('Sales')

plt.tight_layout()
plt.show()

# Conclusion: Both state and school holidays impact sales, with variations in sales patterns. Understanding these patterns helps in planning special promotions and staffing.

# Heatmap for pivot table of Promo vs DayOfWeek
pivot_table = dataframe.pivot_table(index='DayOfWeek', columns='Promo', values='Sales', aggfunc='mean', fill_value=0)
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='.2f', linewidths=.5)
plt.title("Heatmap of Average Sales by DayOfWeek and Promo")
plt.xlabel("Promo")
plt.ylabel("DayOfWeek")
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()

# Conclusion: The heatmap reveals that promotions significantly boost sales across all days of the week. Certain days without promotions still show high sales, suggesting inherent high traffic on those days.
