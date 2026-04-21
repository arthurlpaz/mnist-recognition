from sklearn.metrics import classification_report, confusion_matrix
import numpy as np


def evaluate(model, x_test, y_test):
    preds = model.predict(x_test)
    y_pred = np.argmax(preds, axis=1)

    print(classification_report(y_test, y_pred))
