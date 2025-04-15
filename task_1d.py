import dask
import dask.dataframe as dd
from dask.distributed import Client
import time
import matplotlib.pyplot as plt

# Function to set the task for the processors 
def task(df):
    result = df.groupby('Week')['Number of Trips 10-25'].mean().compute()
    return result

# Read the dataset
parallel_df = dd.read_csv("Trips_by_Distance (1).csv")
# Filter the dataset to national level only
parallel_df = parallel_df[parallel_df['Level'] == 'National']

# Processors
num_of_processors = [10, 20] 
processors_time = {} 

# Run the task with 10 and then 20 processors
for processor in num_of_processors:
    client = Client(n_workers=processor)
    start = time.time()
    task(parallel_df)
    end = time.time()
    running_time = end - start
    processors_time[processor] = running_time
    print(f"{processor} processors - {running_time:.2f} seconds")
    client.close()

# Line plot to compare the time execution difference between 10 and 20 processors
plt.figure(figsize=(14, 6))
plt.plot(processors_time.keys(), processors_time.values(), marker='o', linestyle='-', color = 'orange')
plt.xlabel("Number of Processors")
plt.ylabel("Time (seconds)")
plt.title("Dask Processors Speed Demonstration")
plt.grid(True)
plt.tight_layout()
plt.show()
