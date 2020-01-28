# -*- coding: utf-8 -*-

"""
Module for expackage clustering
"""

from __future__ import absolute_import

import multiprocessing

import hdbscan
import numpy as np
import pickle


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
        # to prevent GUI from freezing
        with multiprocessing.get_context("spawn").Pool() as POOL:
            async_result = POOL.apply_async(
                ClusterGen.fit_cluster, (clusterer, points))
        cluster_results = async_result.get()
        cluster_labels = cluster_results.labels_
        # return cluster points and number of clusters
        mask_noisy = (cluster_labels == -1)
        number_of_clusters = len(
            np.unique(cluster_labels[~mask_noisy]))
        return cluster_labels, number_of_clusters
