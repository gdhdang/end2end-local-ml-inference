from fastapi import FastAPI
from model import predict_model

app = FastAPI(title="Demo End2End ML Inference API")

@app.get("/")
def hello_api():
    return {"msg":"Hello FastAPI🚀"}

@app.post("/predict/", status_code=200)
async def predict():
    score = predict_model()
    return score