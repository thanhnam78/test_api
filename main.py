from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# load model (chỉ chạy 1 lần)
classifier = pipeline(
    "zero-shot-classification",
    model="typeform/distilbert-base-uncased-mnli"
)

# các loại món ăn
labels = [
    "Vietnamese food",
    "Italian food",
    "Fast food",
    "Healthy food", 
    "Japanese food", 
    "Korean food",
    "French food"
]

# input JSON
class InputData(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Food Classification API"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: InputData):
    if not data.text:
        raise HTTPException(status_code=400, detail="Text is required")

    result = classifier(data.text, labels)

    return {
    "input": data.text,
    "result": {
        "label": result["labels"][0],
        "confidence": round(result["scores"][0], 4)
    }
}