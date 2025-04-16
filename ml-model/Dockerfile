FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app/ ./app
CMD ["uvicorn", "app.inference_service:app", "--host", "0.0.0.0", "--port", "80"]
