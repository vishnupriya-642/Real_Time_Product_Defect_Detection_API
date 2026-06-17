from fastapi import FastAPI, File, UploadFile
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = FastAPI(
    title="Real-Time Product Defect Detection",
    description="Deep Learning based defect classification system using CNN and FastAPI",
    version="1.0.0"
)

# Load model
model = tf.keras.models.load_model("model/defect_model.h5")

IMG_SIZE = 128


@app.get("/")
def home():
    return {"message": "Defect Detection API Running"}


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "Product Defect Detection API"
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")

    image = image.resize((IMG_SIZE, IMG_SIZE))
    image = np.array(image)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)

    prediction = model.predict(image)

    score = float(prediction[0][0])

    print("Raw prediction:", score)

    if score > 0.5:
        result = "OK"
        confidence = round(score * 100, 2)
    else:
        result = "Defective"
        confidence = round((1 - score) * 100, 2)

    return {
        "prediction": result,
        "confidence": confidence,
        "raw_score": score
    }