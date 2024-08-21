## CLUSTERING IMPORTS ###

import random

### CLUSTERING FUNCTIONS ###

# Runs the Clustering Algorithm:
def kmeans(data, k, epochs):
  centers = initialize(data, k)
  clusters = []
  for _ in range(epochs):
    distance_matrix = get_distance_matrix(data, centers)
    clusters = assign_clusters(data, centers, distance_matrix)
    centers = find_new_centers(data, clusters)
  return centers, clusters

# Find New Centers:
def find_new_centers(data, clusters):
  new_centers = []
  for i in range(len(clusters)):
    if len(clusters[i]) > 0:
      center = mean(clusters[i])
      new_centers.append(center)
    else:
      new_centers.append(sample_point(data, new_centers))
  return new_centers

# Assign Cluster Function:
def assign_clusters(data, centers, distance_matrix):
  clusters = [[] for _ in range(len(centers))]
  for i in range(len(distance_matrix)):
    index = find_least(distance_matrix[i])
    clusters[index].append(data[i])
  return clusters

# Get Distance Matrix Function:
def get_distance_matrix(data, centers):
  distance_matrix = []
  for point in data:
    point_distances = []
    for center in centers:
      length = distance(point, center)
      point_distances.append(length)
    distance_matrix.append(point_distances)
  return distance_matrix
  
# Initialization Function:
def initialize(data, clusters):
  centers = []
  for _ in range(clusters):
    centers.append(sample_point(data, centers))
  return centers

# Sample Point Function:
def sample_point(data, centers):
  point = data[random.randint(0, len(data)-1)]
  if point not in centers:
    return point
  else:
    return sample_point(data, centers)

### UTILITY FUNCTIONS ###

# Find Least Function:
def find_least(array):
  index = 0
  size = 0
  for i in range(len(array)):
    if i == 0:
      index = i
      size = array[i]
    else:
      if array[i] < size:
        index = i
        size = array[i]
  return index

# Mean Function:
def mean(list):
  x_mean = 0
  y_mean = 0
  for item in list:
    x_mean += item[0]
    y_mean += item[1]
  x_mean /= len(list)
  y_mean /= len(list)
  return x_mean, y_mean

# Distance Function:
def distance(p1, p2):
  return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5