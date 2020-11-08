
import pandas as pd
import numpy as np


import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
random_state = 170
plt.figure(figsize=(3, 5))
'''
    n_samples = 1500
    
    X, y = make_blobs(n_samples=n_samples, random_state=random_state)
'''
df = pd.read_csv( 'full_gps_data.csv',header= None,usecols=[2,3])
X = df.values
# Incorrect number of clusters
y_pred = KMeans(n_clusters=4, random_state=random_state).fit_predict(X)
#print (X,type(X),y,type(y),y_pred,type(y_pred))

#plt.subplot(221)
plt.scatter(X[:, 0], X[:, 1], c=y_pred,alpha = 1,
        s=1.2)
plt.title("K-MEAN n_clusters=4")
'''
# Anisotropicly distributed data
transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
X_aniso = np.dot(X, transformation)
y_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X_aniso)

plt.subplot(222)
plt.scatter(X_aniso[:, 0], X_aniso[:, 1], c=y_pred)
plt.title("Anisotropicly Distributed Blobs")

# Different variance
X_varied, y_varied = make_blobs(n_samples=n_samples,
                                cluster_std=[1.0, 2.5, 0.5],
                                random_state=random_state)
y_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X_varied)

plt.subplot(223)
plt.scatter(X_varied[:, 0], X_varied[:, 1], c=y_pred)
plt.title("Unequal Variance")

# Unevenly sized blobs
X_filtered = np.vstack((X[y == 0][:500], X[y == 1][:100], X[y == 2][:10]))
y_pred = KMeans(n_clusters=3,
                random_state=random_state).fit_predict(X_filtered)

plt.subplot(224)
plt.scatter(X_filtered[:, 0], X_filtered[:, 1], c=y_pred)
plt.title("Unevenly Sized Blobs")
'''
plt.show()