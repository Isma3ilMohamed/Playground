# K-means Clustering
# Import packages and dataset
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from sklearn import datasets

# Import flower species data, iris, to play with
iris_dataset = datasets.load_iris()
# Converting sklearn's dataset into a pandas DataFrame for easy processing
iris_dataset = pd.DataFrame(data=iris_dataset.data, columns=iris_dataset.feature_names)

# Within Cluster Sum of Squares (WCSS), also known as the inertia of clustering
within_cluster_sum_of_squares = []

# Getting the length and width of the input features
# iloc indexer for a Dataframe is used for integer location-based selection of data
# Here, iloc selects all rows and columns 0 to 3
x = iris_dataset.iloc[:, [0, 1, 2, 3]].values

# Changing the numbers of clusters and recording inertia/WCSS
for i in range(1, 6):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(x)
    within_cluster_sum_of_squares.append(kmeans.inertia_)

plt.plot(range(1, 6), within_cluster_sum_of_squares)
plt.title('The elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')  #within cluster sum of squares
plt.show()
