import numpy as np
import pandas as pd
import math
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

data_path = "cars.csv"
actual_clusters = 3
df = pd.read_csv(data_path)
print(df.isnull())
df.dropna(inplace = True)
print(df.isnull())
dim = len(df.columns)
print(dim)

#synthetic data
#df, label = sklearn.datasets.make_blobs(n_samples = 5000, n_features = 4, centers = 10, cluster_std = 1.0)
#dim = 4
#actual_clusters = 10

density = []
for i in range(1,21):
    kmeans_c = KMeans(n_clusters=i, random_state=0).fit_transform(df)
    kmeans_p = KMeans(n_clusters=i, random_state=0).fit_predict(df)
    area=0
    for j in range(0,i):
        output = [[x,y] for x,y in list(zip(kmeans_c[:,j],kmeans_p)) if y==j]
        radius = max(output)[0]
        area += (((np.pi**(dim/2))*(radius**dim))/(math.factorial(int(dim/2))*len(output)))
    density.append((area/i))

plt.plot(range(1, 21), density, '-o')
plt.title("Actual number of clusters {}".format(actual_clusters))
plt.xlabel("Number of Clusters")
plt.ylabel("Mean Cluster Hypersphere Density")
plt.show()