from app import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_prediction_schema():
    payload = {"age": 63, "sex": 1, "cp": 1, "trestbps": 145, "chol": 233, "fbs": 1, 
               "restecg": 2, "thalach": 150, "exang": 0, "oldpeak": 2.3, "slope": 3, 
               "ca": 0, "thal": 6}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()