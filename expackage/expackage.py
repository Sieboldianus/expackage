"""
ExamplePackage:
Demonstrates Joblib Multiprocessing Issue in frozen App
"""

# delay evaluation of annotations at runtime (PEP 563)
from __future__ import absolute_import, annotations

from .classes.cluster import ClusterGen


class ExamplePackage():
    """Perform hdbscan clustering
    """

    def __init__(self):
        """Init settings for ExamplePackage Clustering"""

    def cluster_example(self):
        """Calculate all example clusters"""
        # init
        clusterer = ClusterGen()
        # run cluster
        cluster_labels, number_of_clusters = clusterer.cluster_points()
        # return results
        print(
            f'{number_of_clusters} clusters found. '
            f'Cluster labels: {cluster_labels}')
