# GeoFence

Geographic Location Data Clustering

## Information

This is a KMeans clustering algorithm application for a common data bounding technique called Geofencing. Geofencing is the principle of bounding a geographic region by latitude and longitude. In the case of an unsupervised dataset, the geographic bounds may not be clear. This is a perfect use case for clustering and specifically KMeans clustering. The test dataset generated was for three different cities: New York City, Charlotte, and Miami. This generation algorithm generates a 1000 data points for each of these cities. Then, the clustering algorithm takes over and clusters the data points into three clusters, using the kMeans clustering algorithm. The results are then outputted to the graph ```clusters.png```. 

## Usage

To use the application, simple use the Bash or Batch files listed in the main directory. If you use Windows, run the batch script by running ```geofence.bat``` in the command prompt. If you use MacOS, Linux, or GitBash, run the following command in the terminal: ```bash geofence.sh```.

## Dependencies

- pandas
- numpy
- matplotlib

To install these dependencies simply run the pip commands listed below.

```
pip install pandas
pip install numpy
pip install matplotlib
```