from src.logging.logger import get_logger
from src.pipelines.training_pipeline import run_pipeline
from src.utils.config import load_config  # Assuming you have this based on the config usage


def main():
    config = load_config()

    logger = get_logger("mnist_training")

    run_pipeline(config, logger)


if __name__ == "__main__":
    main()
