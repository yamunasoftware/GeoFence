### DATA IMPORTS ###

import cluster
import knn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

### NORMALIZATION FUNCTIONS ###

# Normalize Function:
def normalize(data):
  latitudes = [x for x, _ in data]
  longitudes = [y for _, y in data]
  
  lat_max = max(latitudes)
  lat_min = min(latitudes)

  long_max = max(longitudes)
  long_min = min(longitudes)

  new_latitudes = []
  for value in latitudes:
    new_latitudes.append(((value - lat_min) / (lat_max - lat_min)))

  new_longitudes = []
  for value in longitudes:
    new_longitudes.append(((value - long_min) / (long_max - long_min)))
  
  normalized = []
  for i in range(len(new_latitudes)):
    normalized.append((new_latitudes[i], new_longitudes[i]))
  
  extrema = [lat_max, lat_min, long_max, long_min]
  return normalized, extrema

# Denormalize Function:
def denormalize(data, extrema):
  latitudes = [x for x, _ in data]
  longitudes = [y for _, y in data]
  
  lat_max = extrema[0]
  lat_min = extrema[1]

  long_max = extrema[2]
  long_min = extrema[3]

  new_latitudes = []
  for value in latitudes:
    new_latitudes.append(((value * (lat_max - lat_min)) + lat_min))

  new_longitudes = []
  for value in longitudes:
    new_longitudes.append(((value * (long_max - long_min)) + long_min))

  denormalized = []
  for i in range(len(new_latitudes)):
    denormalized.append((new_latitudes[i], new_longitudes[i]))
  return denormalized

### DATA PROCESSING AND CLUSTERING ###

# Reads the Datasets:
dataset = pd.read_csv(os.path.join(os.path.pardir, 'dataset.csv'))
test_data = pd.read_csv(os.path.join(os.path.pardir, 'test_data.csv'))

# Filters Datasets:
cluster_set = dataset[['Latitude', 'Longitude']]
label_set = dataset[['Label']]
test_set = test_data[['Latitude', 'Longitude']]

# Gets the Data Lists:
data = list(cluster_set.itertuples(index=False, name=None))
labels = list(label_set.itertuples(index=False, name=None))
test = list(test_set.itertuples(index=False, name=None))

# Normalize All Data:
normalized_data, extrema = normalize(data)
normalized_test, text_extrema = normalize(test)

# Runs Machine Learning Algorithms:
centers, clusters = cluster.kmeans(normalized_data, 3, 3000)
classifications = knn.classifyLists(normalized_test, normalized_data, labels, 3)

# Denormalize Data:
centers = denormalize(centers, extrema)
new_clusters = []
for cluster in clusters:
  new_clusters.append(denormalize(cluster, extrema))

# Gets the Classes:
counts = {}
for label in classifications:
  if label[0] in counts:
    counts[label[0]] += 1
  else:
    counts[label[0]] = 1

### DATA VISUALIZATION ###

# Initialize Data Lists:
x_values = []
y_values = []

# Flattens Clusters into Mapped Points:
for cluster in new_clusters:
  lats = []
  longs = []

  for point in cluster:
    lats.append(point[0])
    longs.append(point[1])
  
  x_values.append(lats)
  y_values.append(longs)

# Sets up the Graph:
plt.figure(figsize=(10,5))
plt.title('GeoFence Clustering')
plt.xlabel('Latitude')
plt.ylabel('Longitude')

# Plots the Clusters:
for i in range(len(x_values)):
  plt.scatter(np.array(x_values[i]), np.array(y_values[i]))

# Plots the Centers of the Clusters:
for center in centers:
  plt.plot(center[0], center[1], 'bo')
plt.savefig(os.path.join(os.path.pardir, 'clusters.png'), bbox_inches='tight')

# Sets up the Graph:
plt.figure(figsize=(10,5))
plt.title('GeoFence Classification')
plt.xlabel('City')
plt.ylabel('Count')

# Gets the Values:
cities = list(counts.keys())
values = list(counts.values())

# Plots Bar Graph:
plt.bar(cities, values)
plt.savefig(os.path.join(os.path.pardir, 'classifications.png'), bbox_inches='tight')
plt.close()