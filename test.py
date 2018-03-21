import numpy as np
from sklearn.cluster import DBSCAN as db
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler

X, labels_true = make_blobs(n_samples=100, centers=3, cluster_std=0.4,
                            random_state=0)
print(labels_true)
X = StandardScaler().fit_transform(X)

db = db(eps=0.3, min_samples=10).fit(X)
'''core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True'''
labels = db.labels_
print(db.labels_)
print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))