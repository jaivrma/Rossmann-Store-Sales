import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from GitHub raw URL
url = r"https://github.com/jaivrma/Rossmann-Store-Sales/blob/main/projectdata.csv"
df = pd.read_csv(url, low_memory=False)

# Print column names to inspect them
print("Column Names:", df.columns)

# Convert 'Date' to datetime type
df["Date"] = pd.to_datetime(df["Date"])

# Check for missing values
print("Missing Values:", df.isnull().sum())

# Fill missing values if necessary (e.g., 'Open' column)
df['Open'].fillna(df["Open"].mode()[0], inplace=True)

# Display data types and basic statistics
print("Data Types:", df.dtypes)
print("Basic Statistics:", df.describe())

# Set the style of the plots
sns.set_style("whitegrid")

# Bar plot for average sales by day of the week
plt.figure(figsize=(10, 6))
avg_sales = df.groupby('DayOfWeek')['Sales'].mean().reset_index()
sns.barplot(x='DayOfWeek', y='Sales', data=avg_sales, palette='viridis')
plt.title('Average Sales by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Average Sales')
plt.show()
# Conclusion: Sales vary across different days of the week, with some days showing higher sales. This indicates customer shopping patterns and store performance variations.

# Effect of promotions on sales
plt.figure(figsize=(10, 6))
avg_promo=df.groupby("Promo")["Sales"].mean().reset_index()
sns.barplot(x='Promo', y='Sales', data=avg_promo, palette='coolwarm')
plt.title('Effect of Promotions on Sales')
plt.xlabel('Promo')
plt.ylabel('Sales')
plt.show()

# Conclusion: Promotions significantly boost sales, showcasing the effectiveness of promotional strategies in increasing revenue.

# Sales distribution on State and School holidays

plt.figure(figsize=(10,6))
avg_state=df.groupby("StateHoliday")["Sales"].mean().reset_index()
sns.barplot(x='StateHoliday', y='Sales', data=avg_state, palette='viridis')
plt.title('Sales Distribution on State Holidays')
plt.xlabel('State Holiday')
plt.ylabel('Sales')
plt.show()

plt.figure(figsize=(10,6))
avg_hol=df.groupby("SchoolHoliday")["Sales"].mean().reset_index()
sns.barplot(x='SchoolHoliday', y='Sales', data=avg_hol, palette='viridis')
plt.title('Sales Distribution on School Holidays')
plt.xlabel('School Holiday')
plt.ylabel('Sales')
plt.show()

# Conclusion: Both state and school holidays impact sales, with variations in sales patterns. Understanding these patterns helps in planning special promotions and staffing.
