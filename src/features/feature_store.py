import numpy as np


class FeatureStore:
    def __init__(self):
        self.store = {}

    def save(self, key, features):
        self.store[key] = features

    def get(self, key):
        return self.store.get(key)
