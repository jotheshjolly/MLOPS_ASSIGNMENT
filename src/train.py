import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score
from eda import load_and_clean_data
import os
import joblib

def train_model():
    df = load_and_clean_data('./data/processed.cleveland.data')
    X = df.drop('target', axis=1)
    y = df['target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    mlflow.set_experiment("ml_ops_mlruns_assignment")

    models = {
        "LogisticRegression": LogisticRegression(C=1.0),
        "RandomForest": RandomForestClassifier(n_estimators=100)
    }

    for name, model in models.items():
        with mlflow.start_run(run_name=name):
            model.fit(X_train_scaled, y_train)
            preds = model.predict(X_test_scaled)
            
            # Log Metrics
            mlflow.log_metric("accuracy", accuracy_score(y_test, preds))
            mlflow.log_metric("precision", precision_score(y_test, preds))
            mlflow.log_metric("recall", recall_score(y_test, preds))
            mlflow.log_metric("roc_auc", roc_auc_score(y_test, preds))
            
            # Log Model
            mlflow.sklearn.log_model(model, "model")
            print(f"{name} logged successfully.")

            model_dir = "models"
            if not os.path.exists(model_dir):
                os.makedirs(model_dir)
            joblib.dump(model, os.path.join(model_dir, "best_model.pkl"))

if __name__ == "__main__":
    train_model()