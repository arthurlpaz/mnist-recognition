import numpy as np

def preprocess_data(x_train, x_test):
    # Normalização
    x_train = x_train / 255.0
    x_test = x_test / 255.0

    # Expandir dimensão (CNN)
    x_train = np.expand_dims(x_train, -1)
    x_test = np.expand_dims(x_test, -1)

    return x_train, x_test