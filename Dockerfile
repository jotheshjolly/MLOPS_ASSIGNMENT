FROM python:3.9-slim

WORKDIR /app

# 1. Copy requirements first (for better caching)
COPY requirements.txt .

# 2. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copy the rest of your code
COPY . .

# 4. Use python -m to run uvicorn
CMD ["python", "-m", "uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]