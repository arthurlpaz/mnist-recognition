import numpy as np


class ModelMonitor:
    def __init__(self):
        self.predictions = []

    def log_prediction(self, pred):
        self.predictions.append(pred)

    def get_stats(self):
        if not self.predictions:
            return {}

        return {
            "total_predictions": len(self.predictions),
            "avg_prediction": float(np.mean(self.predictions)),
        }
