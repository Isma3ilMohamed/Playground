from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Reading MNIST csv file
mnist_dataset = pd.read_csv('/usr/local/notebooks/datasets/csv_datasets/mnist_test.csv')

# Saving the dataset as a pandas DataFrame for easy processing
df = pd.DataFrame(mnist_dataset)
df['label'] = mnist_dataset['label']

# Applying PCA to the data by specifying the number of PCA components
# Play around with n_components: set it to 10 and observe the plot of cumulative variance
pca = PCA(n_components=50)

# Apply PCA to the dataset values (remove labels)
# df.values returns only the values in the DataFrame; axes labels are removed
pca_result = pca.fit_transform(df.values)

# Display results
plt.plot(range(50), pca.explained_variance_ratio_, 'b')    # range(50) generates 50 numbers from 0 to 49
plt.plot(range(50), np.cumsum(pca.explained_variance_ratio_), 'g')
plt.xlabel('Number of principal components')
plt.ylabel('Variance')
plt.legend(['Component-wise variance','Cumulative variance'])
plt.title('Component-wise variance (blue) and and cumulative variance (green)')
plt.show()