# Real-Time Product Defect Detection System

This project implements a real-time product defect detection system using Deep Learning and Computer Vision.  
A trained Convolutional Neural Network (CNN) model is used to classify product images as **Defective** or **OK**.  
The model is deployed through a **FastAPI REST API**, and a **Streamlit interface** is provided for easy interaction and testing.

The system demonstrates how machine learning models can be integrated into production-ready APIs for automated quality inspection in manufacturing environments.

---

## Project Overview

Manual inspection of products in manufacturing lines can be time-consuming and prone to human error.  
Computer Vision and Deep Learning techniques allow automated systems to detect defects quickly and consistently.

This project combines:

- Deep Learning based image classification
- FastAPI for model serving
- Streamlit for user interaction
- Docker for containerized deployment

The goal is to simulate a real-world **machine learning inference service** for defect detection.

---

## Dataset

The model performs **binary image classification** on product images.

Classes:

| Class | Description |
|------|-------------|
| Defective | Product contains visible defect |
| OK | Product does not contain defects |

Before inference, images are processed using:

- Image resizing
- Normalization
- Conversion to numerical arrays
- Batch dimension formatting

---

## Model Architecture

The model used for defect detection is a **Convolutional Neural Network (CNN)** trained using TensorFlow / Keras.

Prediction pipeline:

```
Input Image
      ↓
Image Preprocessing
      ↓
Convolutional Neural Network
      ↓
Dense Classification Layer
      ↓
Binary Prediction
      ↓
Defective / OK
```

The trained model is stored in the project as:

```
model/defect_model.h5
```

---

## System Architecture

```
User Interface (Streamlit)
        │
        ▼
Image Upload
        │
        ▼
FastAPI Backend
        │
        ▼
Image Preprocessing
        │
        ▼
Deep Learning Model (TensorFlow CNN)
        │
        ▼
Prediction Response
```

The architecture separates the **user interface**, **API service**, and **machine learning model inference**.

---

## Technology Stack

Programming Language  
Python

Machine Learning  
TensorFlow  
Keras

Computer Vision  
Pillow  
NumPy

Backend API  
FastAPI  
Uvicorn

User Interface  
Streamlit

Deployment  
Docker

HTTP Communication  
Requests

---

## Project Structure

```
Real_Time_Product_Defect_Detection_API
│
├── model
│   ├── defect_model.h5
│   └── test_images
│
├── app.py
├── main.py
├── Dockerfile
├── requirements.txt
└── README.md
```

Description:

- **main.py** – FastAPI application exposing prediction endpoint  
- **app.py** – Streamlit interface for uploading images and testing predictions  
- **defect_model.h5** – trained CNN model  
- **requirements.txt** – Python dependencies  
- **Dockerfile** – container configuration for deployment  

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Real_Time_Product_Defect_Detection_API.git
cd Real_Time_Product_Defect_Detection_API
```

Install required dependencies

```bash
pip install -r requirements.txt
```

---

## Running the FastAPI Server

Start the API server

```bash
uvicorn main:app --reload
```

The API will run at:

```
http://127.0.0.1:8000
```

Interactive API documentation is available at:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoint

### Predict Product Defect

POST request

```
/predict
```

The endpoint accepts an image file and returns a prediction.

Example response

```json
{
  "prediction": "Defective"
}
```

---

## Running the Streamlit Interface

The Streamlit interface allows users to upload product images and send them to the FastAPI server.

Run the interface with:

```bash
streamlit run app.py
```

The browser interface will allow users to test the model predictions interactively.

---

## Docker Deployment

Build Docker image

```bash
docker build -t defect-detection-api .
```

Run container

```bash
docker run -p 8000:8000 defect-detection-api
```

The application will be accessible at

```
http://localhost:8000
```

---

## Applications

- Automated manufacturing inspection
- Product quality monitoring
- Industrial computer vision systems
- Smart factory automation

---

## Future Improvements

- Real-time camera integration
- Model retraining pipeline
- Performance monitoring and logging
- Edge deployment on embedded devices
- CI/CD pipeline for automated deployment

---

## Author

Vishnupriya V  
