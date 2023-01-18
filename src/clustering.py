import numpy as np
import pandas as pd

from sklearn.decomposition import PCA
from sklearn.cluster import KMeans


def reduce_dimensions(data, labels):
    filenames = np.array(list(data.keys()))
    features = np.array(list(data.values()))

    features = features.reshape(-1, 4096)

    df = pd.read_csv(labels)
    label = df["label"].tolist()
    unique_labels = list(set(label))

    pca = PCA(n_components=100, random_state=23)
    pca.fit(features)
    reduced_features = pca.transform(features)

    return filenames, unique_labels, reduced_features


def create_clusters(filenames, labels, features):
    clusters = {}
    kmeans = KMeans(n_clusters=len(labels), n_jobs=1, random_state=23)
    kmeans.fit(features)

    for file, cluster in zip(filenames, kmeans.labels_):
        if cluster not in clusters.keys():
            clusters[cluster] = []
            clusters[cluster].append(file)
        else:
            clusters[cluster].append(file)

    return clusters
