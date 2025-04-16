from fastapi import FastAPI, Request
from model import predict

app = FastAPI()

@app.post("/predict")
async def predict_endpoint(request: Request):
    data = await request.json()
    result = predict(data)
    return result
