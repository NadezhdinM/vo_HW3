from fastapi import FastAPI, HTTPException
from transformers import pipeline
from pydantic import BaseModel

app = FastAPI()

classifier = pipeline("sentiment-analysis")

class Item(BaseModel):
    text: str

@app.post("/predict/")
def predict(item: Item):
    try:
        result = classifier(item.text)

        sentiment = result[0]['label']
        confidence = result[0]['score']

        return {"sentiment": sentiment, "confidence": confidence}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
