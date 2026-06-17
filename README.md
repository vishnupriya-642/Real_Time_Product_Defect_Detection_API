# Real-Time Product Defect Detection System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Live-green)
![Docker](https://img.shields.io/badge/Docker-Deployed-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-CNN-orange)
![Render](https://img.shields.io/badge/Render-Cloud-purple)

## Overview

This project implements a Real-Time Product Defect Detection System using Deep Learning and Computer Vision.

A trained Convolutional Neural Network (CNN) model is used to classify product images as:

* Defective
* OK

The model is deployed through a FastAPI REST API and containerized using Docker for cloud deployment.

The application is currently deployed and accessible through Render Cloud.

---

## Live Deployment

### API Base URL

https://real-time-product-defect-detection-api.onrender.com

### Swagger Documentation

https://real-time-product-defect-detection-api.onrender.com/docs

### Health Endpoint

https://real-time-product-defect-detection-api.onrender.com/health

---

## Project Highlights

✔ CNN-Based Defect Detection

✔ FastAPI REST API

✔ Docker Containerization

✔ TensorFlow Deep Learning Model

✔ Cloud Deployment on Render

✔ Confidence Score Prediction

✔ Swagger API Documentation

✔ Health Monitoring Endpoint

✔ Production Ready Deployment

---

## Problem Statement

Manual product inspection in manufacturing environments can be:

* Time-consuming
* Expensive
* Inconsistent
* Error-prone

This project demonstrates how Deep Learning can automate quality inspection and improve manufacturing efficiency through image-based defect detection.

---

## Dataset

The model performs binary image classification on product images.

### Classes

| Class     | Description                         |
| --------- | ----------------------------------- |
| Defective | Product contains visible defects    |
| OK        | Product contains no visible defects |

### Preprocessing Pipeline

Before prediction:

* Image resizing
* RGB conversion
* Pixel normalization
* NumPy conversion
* Batch dimension creation

---

## Model Architecture

The defect detection model is built using TensorFlow/Keras and Convolutional Neural Networks (CNN).

### Prediction Pipeline

Input Image

↓

Image Preprocessing

↓

CNN Feature Extraction

↓

Dense Classification Layer

↓

Binary Classification

↓

Defective / OK

---

## Model File

The trained model is stored as:

model/defect_model.h5

---

## System Architecture

User

↓

FastAPI REST API

↓

Image Preprocessing

↓

TensorFlow CNN Model

↓

Prediction Response

---

## Cloud Architecture

Client Request

↓

Render Cloud

↓

Docker Container

↓

FastAPI Application

↓

TensorFlow Model

↓

Prediction Response

---

## Technology Stack

### Programming Language

* Python

### Machine Learning

* TensorFlow
* Keras

### Computer Vision

* Pillow
* NumPy

### Backend

* FastAPI
* Uvicorn

### Frontend

* Streamlit

### Containerization

* Docker

### Cloud Deployment

* Render

### API Testing

* Swagger UI

---

## Project Structure

Real_Time_Product_Defect_Detection_API

├── model

│ ├── defect_model.h5

│ └── test_images

│

├── app.py

├── main.py

├── Dockerfile

├── requirements.txt

├── README.md

└── .dockerignore

### File Description

* main.py → FastAPI backend service
* app.py → Streamlit user interface
* defect_model.h5 → Trained CNN model
* Dockerfile → Docker container configuration
* requirements.txt → Python dependencies
* README.md → Project documentation

---

## Installation

### Clone Repository

```bash
git clone https://github.com/vishnupriya-642/Real_Time_Product_Defect_Detection_API.git

cd Real_Time_Product_Defect_Detection_API
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Running FastAPI Server

```bash
uvicorn main:app --reload
```

API URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Home Endpoint

```http
GET /
```

Response:

```json
{
  "message": "Defect Detection API Running"
}
```

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "healthy",
  "service": "Product Defect Detection API"
}
```

### Predict Product Defect

```http
POST /predict
```

Upload an image file and receive prediction results.

Example Response:

```json
{
  "prediction": "Defective",
  "confidence": 68.1,
  "raw_score": 0.319
}
```

---

## Running Streamlit Interface

Launch the user interface:

```bash
streamlit run app.py
```

Users can upload product images and receive prediction results through a simple web interface.

---

## Docker Deployment

### Build Docker Image

```bash
docker build -t defect-detection-api .
```

### Run Docker Container

```bash
docker run -p 8000:8000 defect-detection-api
```

Application URL:

```text
http://localhost:8000
```

---

## Deployment on Render

This project is deployed using:

* GitHub
* Docker
* Render Cloud

Deployment URL:

https://real-time-product-defect-detection-api.onrender.com

---

## Key Features

* Deep Learning based image classification
* Real-time defect detection
* TensorFlow CNN inference
* Confidence score generation
* REST API architecture
* Docker containerization
* Cloud deployment
* Health monitoring endpoint
* Interactive Swagger documentation

---

## Applications

* Manufacturing Quality Inspection
* Automated Product Validation
* Smart Factory Automation
* Industrial Computer Vision
* AI-based Quality Control Systems

---

## Future Enhancements

### Machine Learning

* Multi-class defect detection
* Transfer Learning Models
* YOLO Object Detection
* Model Monitoring

### DevOps

* GitHub Actions CI/CD
* Kubernetes Deployment
* AWS ECS Deployment
* Azure Container Apps

### Production Features

* Real-Time Camera Integration
* Batch Image Processing
* Database Logging
* Monitoring Dashboard

---

## Screenshots

Add screenshots here:

### Swagger Documentation

images/swagger.png

### Prediction Results

images/prediction.png

### Render Deployment

images/render.png

---

## Resume Highlights

Developed and deployed a Real-Time Product Defect Detection System using TensorFlow CNN, FastAPI, Docker, and Render Cloud. Implemented image classification APIs with confidence scoring, health monitoring endpoints, and cloud-based deployment for production-ready inference.

---

## Author

Vishnupriya V

Machine Learning Engineer

Skills:

Python | TensorFlow | FastAPI | Docker | Deep Learning | Computer Vision | Machine Learning | Cloud Deployment
