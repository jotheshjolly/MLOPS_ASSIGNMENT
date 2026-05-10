from fastapi import FastAPI
import uvicorn
import logging
import pandas as pd
import mlflow.sklearn
import joblib
import os
import time

MODEL_PATH = os.path.join("models", "best_model.pkl")

app = FastAPI()
# Configure logging to write to both console and a file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("api_logs.log"), logging.StreamHandler()]
)
logger = logging.getLogger("HeartDiseaseAPI")

# Load model logic
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    # This ensures the API starts even if training hasn't run, 
    # but provides a warning/error logic
    model = None
    print(f"Warning: Model not found at {MODEL_PATH}. Run training first.")

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict")
def predict(data: dict):
    if model is None:
        return {"error": "Model not trained yet"}, 503
    logger.info(f"Received request: {data}")
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    confidence = model.predict_proba(df).max()
    result = {"prediction": int(prediction), "confidence": float(confidence)}
    logger.info(f"Prediction: {result}")
    return result

@app.middleware("http")
async def log_requests(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    logger.info(f"Path: {request.url.path} Duration: {duration:.4f}s Status: {response.status_code}")
    return response