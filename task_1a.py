import pandas as pd
import matplotlib.pyplot as plt

# Open the dataset
trips_full = pd.read_csv("Trips_Full Data (2).csv")

# Check missing values
full_data_null = trips_full.isnull().sum()
print(full_data_null)

# Convert the ‘Date’ column to the date/time format
trips_full['Date'] = pd.to_datetime(trips_full['Date'])

# Check total number of people staying at Home
people_staying = trips_full['Population Staying at Home'].sum()
print(f"Total number of people staying at home across all dates: {people_staying}")

# Check total number of people not staying at home
people_not_staying = trips_full['People Not Staying at Home'].sum()
print(f"Total number of people not staying at home across all dates: {people_not_staying}")

# Plot the bar chart to compare 
labels = ['Staying at Home', 'Not Staying at Home']
values = [people_staying, people_not_staying]
plt.figure(figsize=(12, 8))
plt.bar(labels, values, color=['blue', 'orange'])
plt.ylabel('Total People (M)')
plt.title('Total People Staying at Home vs Not Staying at Home')
plt.show()

# Pull all of the distance columns for plotting 
distance_columns = [
    'Trips <1 Mile',
    'Trips 1-3 Miles',
    'Trips 3-5 Miles',
    'Trips 5-10 Miles',
    'Trips 10-25 Miles',
    'Trips 25-50 Miles',
    'Trips 50-100 Miles',
    'Trips 100-250 Miles',
    'Trips 250-500 Miles',
    'Trips 500+ Miles'
]

# Avarage of each column
avg_trips_distance = trips_full[distance_columns].mean()

# Bar chart to show the average number of people on each distance range
plt.figure(figsize=(12, 6))
avg_trips_distance.plot(kind='bar', color='blue')
plt.title('Average Number of People per Trip Distance')
plt.xlabel('Trip Distance Range')
plt.ylabel('Average Number of People (in hundreds of millions)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
