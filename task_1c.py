import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load data
trips_full = pd.read_csv("Trips_Full Data (2).csv")
trips_distance = pd.read_csv("Trips_by_Distance (1).csv")

# Extract the relevant columns
x_data = trips_full['Trips 1-25 Miles']
y_data = trips_distance['Number of Trips 5-10']

# Combine the columns and drop missing values
df = pd.concat([x_data, y_data], axis=1).dropna()

# Reshape for sklearn
x = df['Trips 1-25 Miles'].values.reshape(-1, 1)
y = df['Number of Trips 5-10'].values.reshape(-1, 1)

# Build and train the model
model = LinearRegression()
model.fit(x, y)

# Get results
r_sq = model.score(x, y)
y_predict = model.predict(x)

# Output r-squared coefficient
print(f"Coefficient of Determination: {r_sq}")

# Scatter plot to show the results
plt.scatter(x, y, color='blue', label='Actual Data')
plt.plot(x, y_predict, color='red', label='Predicted Line')
plt.xlabel("Trips 1-25 Miles")
plt.ylabel("Number of Trips 5-10")
plt.title("Linear Regression: Trips 1-25 Miles vs Trips 5-10")
plt.legend()
plt.grid(True)
plt.show()
