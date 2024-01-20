import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer

# Load the network data from the CSV file
df = pd.read_csv('SDN_traffic.csv')

# Display basic information about the dataset
print("shape:", df.shape)
print("\nFirst few rows:")
print(df.head())
print("\nDetail statistics informations:")
print(df.describe())

# Drop unnecessary columns (if needed)
# df.drop(['column_name1', 'column_name2'], axis=1, inplace=True)
# df.rename(columns={'old_name': 'new_name'}, inplace=True)

# # Impute missing values using a constant strategy
imputer = SimpleImputer(strategy='constant', fill_value=0)
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

# Group data by specific columns and aggregate values
df_grouped = df_imputed.groupby(['category']).agg({
    'forward_pps_mean': 'mean',
    'reverse_pps_mean': 'mean',
    'forward_duration': 'sum',
    'reverse_duration': 'sum'
}).reset_index()

# Display the grouped data
print("\nGrouped Data:")
print(df_grouped)

# Plotting examples
plt.figure(figsize=(12, 6))

# Bar plot of mean forward and reverse PPS for each category
plt.subplot(1, 2, 1)
df_grouped.plot(x='category', y=['forward_pps_mean', 'reverse_pps_mean'], kind='bar', title='Mean PPS by Category', rot=0)
plt.ylabel('Mean PPS')

# Pie chart of total duration for each category
plt.subplot(1, 2, 2)
df_grouped.plot.pie(y='forward_duration', labels=df_grouped['category'], autopct='%1.1f%%', startangle=90, title='Total Forward Duration')
plt.ylabel('')  # Remove y-axis label for better presentation

plt.tight_layout()
plt.show()
