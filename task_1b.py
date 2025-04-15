import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
trips_distance = pd.read_csv("Trips_by_Distance (1).csv")

# Check missing values
distance_data_null = trips_distance.isnull().sum()
print(distance_data_null)

# Drop rows where columns below have a null value
clean_trips_distance = trips_distance.dropna(subset=[
    'Population Staying at Home',
    'Population Not Staying at Home',
    'Number of Trips'
])

# Drop the columns not needed for data analysis
clean_trips_distance = clean_trips_distance.drop(columns=[
    'State FIPS', 'State Postal Code', 'County FIPS', 'County Name'
])

print(clean_trips_distance.isnull().sum())

# Convert the 'Date' column to the date/time 
clean_trips_distance['Date'] = pd.to_datetime(clean_trips_distance['Date'])

# Filter the dataset to national level only
national = clean_trips_distance[clean_trips_distance['Level'] == 'National']

# Filter to get number of trips with more than 10,000,000 people 
trips_10_25 = national[national['Number of Trips 10-25'] > 10000000]
trips_50_100 = national[national['Number of Trips 50-100'] > 10000000]

# Scatterplot to compare dates number of people that travelled different distances 
plt.figure(figsize=(14, 6))
plt.scatter(trips_10_25['Date'], trips_10_25['Number of Trips 10-25'], label='Trips 10–25 Miles', color='blue', alpha=0.7)
plt.scatter(trips_50_100['Date'], trips_50_100['Number of Trips 50-100'], label='Trips 50–100 Miles', color='orange', alpha=0.7)
plt.xlabel('Date')
plt.ylabel('Number of Trips')
plt.title('Dates When >10M People Traveled (10–25 vs 50–100 Miles)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
