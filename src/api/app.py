from fastapi import FastAPI, UploadFile, File
from PIL import Image

from src.models.inference import ModelService
from src.monitoring.monitor import ModelMonitor

app = FastAPI()

model_service = ModelService("models/model.h5")
monitor = ModelMonitor()


@app.get("/")
def health():
    return {"status": "ok"}


@app.post("/predict-image")
async def predict_image(file: UploadFile = File(...)):
    image = Image.open(file.file)

    digit = model_service.predict_from_image(image)

    monitor.log_prediction(digit)

    return {"digit": digit}


@app.get("/metrics")
def metrics():
    return monitor.get_stats()
