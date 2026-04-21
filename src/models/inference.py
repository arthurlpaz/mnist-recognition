import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image


class ModelService:
    def __init__(self, model_path: str):
        self.model = load_model(model_path)

    def preprocess_array(self, image_array: np.ndarray):
        image = image_array / 255.0
        image = np.expand_dims(image, -1)
        image = np.expand_dims(image, 0)
        return image

    def preprocess_image(self, image: Image.Image):
        image = image.convert("L")
        image = image.resize((28, 28))

        img_array = np.array(image) / 255.0
        img_array = img_array.reshape(1, 28, 28, 1)

        return img_array

    def predict(self, processed_image: np.ndarray):
        pred = self.model.predict(processed_image)
        return int(np.argmax(pred))

    def predict_from_array(self, image_array: np.ndarray):
        processed = self.preprocess_array(image_array)
        return self.predict(processed)

    def predict_from_image(self, image: Image.Image):
        processed = self.preprocess_image(image)
        return self.predict(processed)
