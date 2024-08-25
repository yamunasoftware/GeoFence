### kNN FUNCTIONS ###

# Classify Data Lists:
def classifyLists(points, data, labels, k):
  classifications = []
  for point in points:
    classifications.append(classifyNN(point, data, labels, k))
  return classifications

# Gets the NN Classification:
def classifyNN(point, data, labels, k):
  indexes = findNN(point, data, k)
  nn_labels = [labels[i] for i in indexes]

  label_counts = {}
  for label in nn_labels:
    if label in label_counts:
      label_counts[label] += 1
    else:
      label_counts[label] = 1

  predicted_label = max(label_counts, key=label_counts.get)
  return predicted_label

# Find NN Distances:
def findNN(point, data, k):
  distances = []
  indices = []

  for i in range(len(data)):
    distances.append(distance(point, data[i]))
    indices.append(i)
  
  sortable = list(zip(distances, indices))
  sortable.sort(key=lambda tup: tup[0])
  indexes = [tup[1] for tup in sortable[:k]]
  return indexes

# Distance Function:
def distance(p1, p2):
  return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5