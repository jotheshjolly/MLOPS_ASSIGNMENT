# MLOPS_ASSIGNMENT
Complete MLOps Pipeline: EDA, Training, and K8s Deployment 2025cs05046

Here is the proper Markdown code. You can use the copy button in the top right corner of the block to easily copy and paste it into your `README.md` file on GitHub:

```markdown
# Heart Disease Prediction MLOps

This repository contains an end-to-end Machine Learning Operations (MLOps) pipeline for predicting heart disease. It includes scripts for model training, a FastAPI-based inference service, containerization configurations, and Kubernetes deployment manifests.

## 📁 Repository Structure

* **`app.py`**: FastAPI application serving the ML model as a REST API.
* **`train.py`**: Script for data preprocessing and model training using `pandas` and `scikit-learn`.
* **`test_api.py`**: Automated test suite for the API endpoints.
* **`Dockerfile`**: Docker containerization instructions using a Python 3.9 slim base image.
* **`requirements.txt`**: Python dependencies required for the project.
* **`deployment.yaml`**: Kubernetes manifest for managing the API container deployment.
* **`service.yaml`**: Kubernetes manifest for exposing the API service.
* **`pytest.ini`**: Configuration file for the pytest testing framework.

## 🚀 Getting Started

### Prerequisites

* Python 3.9+
* Docker
* Kubernetes cluster (e.g., Minikube, kind, or cloud-managed K8s)

### 1. Local Development Setup

Clone the repository and install the required dependencies:

```bash
git clone <your-repository-url>
cd heart-disease-mlops
pip install -r requirements.txt

```

### 2. Model Training

Run the training script to process the data and generate the model artifacts:

```bash
python train.py

```

### 3. Running the API

Start the FastAPI server locally:

```bash
uvicorn app:app --reload

```

The API will be available at `http://localhost:8000`. You can view the interactive Swagger documentation at `http://localhost:8000/docs`.

### 4. Running Tests

Execute the automated tests using pytest:

```bash
pytest

```

## 🐳 Containerization with Docker

Build and run the application as a Docker container:

1. **Build the Docker image:**
```bash
docker build -t heart-disease-api .

```


2. **Run the container:**
```bash
docker run -p 8000:8000 heart-disease-api

```



## ☸️ Kubernetes Deployment

Deploy the containerized API to your Kubernetes cluster:

1. **Apply the Deployment configuration:**
```bash
kubectl apply -f deployment.yaml

```


2. **Apply the Service configuration:**
```bash
kubectl apply -f service.yaml

```



## 🛠️ Tech Stack

* **Language:** Python 3.9
* **Web Framework:** FastAPI, Uvicorn
* **Machine Learning:** scikit-learn, pandas
* **Testing:** pytest
* **DevOps:** Docker, Kubernetes

