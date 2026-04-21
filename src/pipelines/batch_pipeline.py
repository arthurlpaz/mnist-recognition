from src.batch.batch_inference import run_batch


def run_batch_pipeline():
    preds = run_batch()

    with open("reports/batch_predictions.txt", "w") as f:
        f.write(str(preds))
