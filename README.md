# 📰 Fake News Detector API

This project provides an API that summarizes a news article and predicts whether the content is **FAKE** or **REAL** using transformer-based NLP models.

---

## 🚀 Features
- Text Summarization (DistilBART model)
- Fake News Detection (BERT Tiny model)
- REST API with FastAPI
- Can be deployed to Render, Railway, AWS, or other cloud providers

---

## 📂 Repository Structure

```
fake-news-detector/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/fake-news-detector.git
cd fake-news-detector
```

### 2️⃣ Install Required Packages

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

> 💡 Make sure Python 3.8+ is installed.

---

## ▶️ Running the API Locally

Start the server:

```bash
uvicorn app:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Interactive Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Usage

### Endpoint:
```
POST /analyze
```

### Request Body Example:

```json
{
  "text": "Your article text here"
}
```

### Response Example:
```json
{
  "summary": "This is the summarized content...",
  "label": "FAKE",
  "confidence": 0.9132,
  "fake_probability": 0.9132,
  "real_probability": 0.0867
}
```

---

## 🌍 Deployment (Render Recommended)

1. Push repository to GitHub
2. Go to https://render.com
3. Click **New → Web Service**
4. Select your GitHub repository
5. Use the settings below:

| Setting | Value |
|--------|-------|
| Runtime | Python |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `uvicorn app:app --host 0.0.0.0 --port 10000` |

Click **Deploy** 🎉

---

## 🎨 Frontend Integration Example

```javascript
fetch("https://your-api-url.onrender.com/analyze", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ text: userInput })
})
.then(res => res.json())
.then(data => console.log(data));
```

---

## ❤️ Contributing

Feel free to fork this repository and submit PRs!

---

## 📄 License
This project is open-source under the **MIT License**.
