# -*- coding: utf-8 -*-

"""
Module for expackage clustering
"""

from __future__ import absolute_import

import multiprocessing

import hdbscan
import numpy as np
import pickle

# spawn is default for windows
# simulate same behaviour in linux
multiprocessing.set_start_method('spawn')
POOL = multiprocessing.Pool(processes=1)


class ClusterGen():
    def __init__(self):
        """Init ClusterGen"""
        return

    @staticmethod
    def fit_cluster(clusterer, data):
        """Perform HDBSCAN clustering from features or distance matrix.
        Args:
            clusterer ([type]): HDBScan clusterer
            data ([type]): A feature array (points)
        Returns:
            [type]: Clusterer
        """
        clusterer.fit(data)
        return clusterer

    def cluster_points(self):
        """Cluster points using HDBSCAN"""
        # load pickle sample point data
        with open('points.pkl', 'rb') as f:
            points = pickle.load(f)
        clusterer = hdbscan.HDBSCAN(
            min_cluster_size=2,
            gen_min_span_tree=False,
            allow_single_cluster=True,
            min_samples=1)
        # Start clusterer on different thread
        async_result = POOL.apply_async(
            ClusterGen.fit_cluster, (clusterer, points))
        # get results from clusterer
        cluster_results = async_result.get()
        # process results
        cluster_labels = cluster_results.labels_
        # return cluster points and number of clusters
        mask_noisy = (cluster_labels == -1)
        number_of_clusters = len(
            np.unique(cluster_labels[~mask_noisy]))
        return cluster_labels, number_of_clusters
