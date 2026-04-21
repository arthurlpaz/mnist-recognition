import mlflow
import mlflow.keras


def train_model(model, x_train, y_train, config):
    with mlflow.start_run():

        mlflow.log_params(config["training"])

        model.fit(
            x_train,
            y_train,
            epochs=config["training"]["epochs"],
            batch_size=config["training"]["batch_size"],
        )

        mlflow.keras.log_model(model, "model")
