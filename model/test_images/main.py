from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import tensorflow as tf
import numpy as np
from PIL import Image
import io

# Create FastAPI app
app = FastAPI()

# Load trained model
model = tf.keras.models.load_model("defect_model.h5")

# Image size used during training
IMG_SIZE = 128


# Home route
@app.get("/")
def home():
    return {"message": "Real-Time Product Defect Detection API is running"}


# Prediction route
@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    # Read image file
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    # Resize image
    image = image.resize((IMG_SIZE, IMG_SIZE))

    # Convert to numpy array
    image = np.array(image)

    # Normalize
    image = image / 255.0

    # Add batch dimension
    image = np.expand_dims(image, axis=0)

    # Predict
    prediction = model.predict(image)

    # Binary classification threshold
    if prediction[0][0] > 0.5:
        result = "Defective"
    else:
        result = "OK"

    return JSONResponse(content={"prediction": result})