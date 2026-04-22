import numpy as np
from tensorflow.keras.datasets import mnist

from src.models.inference import ModelService

model_service = ModelService("models/model.keras")


def run_batch():
    (_, _), (x_test, _) = mnist.load_data()

    predictions = []

    for img in x_test[:100]:
        pred = model_service.predict_from_array(img)
        predictions.append(pred)

    return predictions


if __name__ == "__main__":
    preds = run_batch()
    print(preds[:10])
