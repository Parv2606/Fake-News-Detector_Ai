from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Load models once (important for performance)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
detector = pipeline("text-classification", model="mrm8488/bert-tiny-finetuned-fake-news-detection")

class Article(BaseModel):
    text: str

@app.post("/analyze")
def analyze(article: Article):
    text = article.text

    summary = summarizer(text, max_length=120, min_length=30, do_sample=False)[0]["summary_text"]
    all_scores = detector(text, return_all_scores=True)[0]

    fake = real = 0.0
    for item in all_scores:
        label = item["label"].upper()
        score = float(item["score"])
        if "FAKE" in label:
            fake = score
        if "REAL" in label or "TRUE" in label:
            real = score

    label = "FAKE" if fake >= real else "REAL"
    confidence = max(fake, real)

    return {
        "summary": summary,
        "label": label,
        "confidence": round(confidence, 4),
        "fake_probability": round(fake, 4),
        "real_probability": round(real, 4),
    }

# For local testing
# Run using: uvicorn app:app --reload
