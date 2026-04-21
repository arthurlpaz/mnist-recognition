from src.data.loader import load_data
from src.data.preprocessing import preprocess_data
from src.models.architecture import build_model
from src.models.trainer import train_model
from src.evaluation.evaluator import evaluate


def run_pipeline(config, logger):
    logger.info("Loading data...")
    x_train, x_test, y_train, y_test = load_data()

    logger.info("Preprocessing...")
    x_train, x_test = preprocess_data(x_train, x_test)

    logger.info("Building model...")
    model = build_model(config)

    logger.info("Training...")
    train_model(model, x_train, y_train, config)

    logger.info("Evaluating...")
    evaluate(model, x_test, y_test)

    logger.info("Saving model...")
    model.save(config["paths"]["model_output"])
