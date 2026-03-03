from fastapi import FastAPI, File, UploadFile
import tensorflow as tf
import numpy as np
from PIL import Image
import io

# 👇 PUT IT HERE (Replace app = FastAPI())
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


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    # Read image
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")

    # Resize
    image = image.resize((IMG_SIZE, IMG_SIZE))

    # Convert to numpy
    image = np.array(image)

    # Normalize
    image = image / 255.0

    # Add batch dimension
    image = np.expand_dims(image, axis=0)

    # Predict
    prediction = model.predict(image)

    if prediction[0][0] > 0.5:
        result = "Defective"
    else:
        result = "OK"

    return {"prediction": result}