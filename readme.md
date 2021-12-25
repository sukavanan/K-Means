#Identifying the number of clusters for K-Means: A hypersphere density based approach

Introduced a novel algorithm to identify the number of clusters in a dataset for K-Means by considering the d-dimensional hypersphere densities of the clusters as the deciding factor. Compared the results of the algorithm with the likes of Elbow Method and Silhouette Score on both toy datasets and synthetic datasets and found that the hypersphere algorithm performs equally good or better than the other two algorithms on all occassions. The paper can be read at - https://arxiv.org/abs/1912.00643.

The hypersphere.py file has runs the algorithm on a sample dataset and displays the hypersphere density vs. number of clusters graph.

The outputs folder contains output graphs of all three methods (elb - Elbow, sil - Silhouette Score, res - Hypersphere Density) on both toy and synthetic datasets.