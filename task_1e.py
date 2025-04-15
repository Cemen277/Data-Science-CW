import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
trips_full = pd.read_csv("Trips_Full Data (2).csv")

# Pick relevant distance columns
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

# Sum the distance columns to get total number of trips per distance
distance_sums = trips_full[distance_columns].sum()

# Bar plot to show the distribution of trips number over the distances 
plt.figure(figsize=(10, 6))
distance_sums.plot(kind='bar', color='skyblue')
plt.title("Total Trips by Distance Category (Week 32)")
plt.xlabel("Distance Range")
plt.ylabel("Total Number of Trips")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
