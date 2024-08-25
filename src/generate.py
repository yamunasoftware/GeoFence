### GENERATION IMPORTS ###

import os
import random
import pandas as pd

### DATASET GENERATION ###

# Latitude and Longitude Bounds:
latitude_bounds = [(40.4774, 40.9176), (35.0194, 35.4214), (25.7090, 25.8557)]
longitude_bounds = [(73.7004, 74.2591), (80.6431, 81.0481), (80.1391, 80.3199)]
labels = ['New York', 'Charlotte', 'Miami']

# Generates Random Points:
points = []
for _ in range(1000):
  for i in range(len(latitude_bounds)):
    latitude = random.uniform(latitude_bounds[i][0], latitude_bounds[i][1])
    longitude = random.uniform(longitude_bounds[i][0], longitude_bounds[i][1])
    points.append((latitude, longitude, labels[i]))

# Save Dataframe to CSV:
dataset = pd.DataFrame(points, columns=['Latitude', 'Longitude', 'Label'])
dataset.to_csv(os.path.join(os.path.pardir, 'dataset.csv'), index=False)

# Generates Test Data:
test_points = []
for _ in range(50):
  for i in range(len(latitude_bounds)):
    latitude = random.uniform(latitude_bounds[i][0], latitude_bounds[i][1])
    longitude = random.uniform(longitude_bounds[i][0], longitude_bounds[i][1])
    test_points.append((latitude, longitude))

# Save Test Dataframe to CSV:
test_data = pd.DataFrame(test_points, columns=['Latitude', 'Longitude'])
test_data.to_csv(os.path.join(os.path.pardir, 'test_data.csv'), index=False)