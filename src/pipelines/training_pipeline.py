from src.data.loader import load_data
from src.data.preprocessing import preprocess_data
from src.models.architecture import build_model
from src.models.trainer import train_model
from src.evaluation.evaluator import evaluate
from src.features.feature_store import FeatureStore


def run_pipeline(config):
    feature_store = FeatureStore()

    x_train, x_test, y_train, y_test = load_data()
    x_train, x_test = preprocess_data(x_train, x_test)

    feature_store.save("train", x_train)
    feature_store.save("test", x_test)

    model = build_model(config)

    train_model(model, x_train, y_train, config)
    evaluate(model, x_test, y_test)

    model.save(config["paths"]["model_output"])
