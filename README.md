# 📰 Fake News Detector (Streamlit App)

This project analyzes news articles and determines whether the information is **REAL** or **FAKE**, while also generating a **smart AI summary**.

It uses:
- DistilBART (summarization)
- BERT Tiny Finetuned Model (Fake vs Real Classification)
- Streamlit UI
- Hosted Free on Hugging Face (never sleeps)

---

## ✅ Features
- AI Summary of article
- Fake vs Real classification
- Confidence scores
- Beautiful glass UI
- Can be hosted free

---

## 📦 requirements.txt

```
streamlit
transformers
sentencepiece
torch --index-url https://download.pytorch.org/whl/cpu
```

---

## 🧠 app.py

Copy this into app.py:

```
import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Fake News Detector", page_icon="📰", layout="centered")

@st.cache_resource
def load_models():
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    detector = pipeline("text-classification", model="mrm8488/bert-tiny-finetuned-fake-news-detection")
    return summarizer, detector

summarizer, detector = load_models()

st.markdown("""
<style>
body {
    background: linear-gradient(120deg, #4b8bff, #8f41ff);
}
.reportview-container, .block-container {
    background: rgba(255,255,255,0.14) !important;
    backdrop-filter: blur(15px);
    border-radius: 16px;
    padding: 45px;
    color: white !important;
}
textarea, .stTextArea textarea {
    background: rgba(255,255,255,0.75) !important;
    color: black !important;
    border-radius: 12px !important;
    font-size: 16px !important;
}
.stButton>button {
    background: #ffce00 !important;
    color: black !important;
    font-weight: bold !important;
    border-radius: 14px !important;
    padding: 10px 20px;
}
.stButton>button:hover {
    background: #ffb300 !important;
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

st.title("📰 Fake News Detector")
st.write("Analyze news articles for credibility and summary.")

article = st.text_area("Paste article text here:", placeholder="Paste your news article...")

if st.button("Analyze"):
    if article.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        with st.spinner("Analyzing..."):
            summary = summarizer(article, max_length=120, min_length=30, do_sample=False)[0]["summary_text"]
            results = detector(article, return_all_scores=True)[0]

            fake = real = 0
            for r in results:
                if "FAKE" in r["label"].upper(): fake = r["score"]
                if "REAL" in r["label"].upper() or "TRUE" in r["label"].upper(): real = r["score"]

            label = "FAKE" if fake >= real else "REAL"
            confidence = max(fake, real)

        st.subheader("📌 Summary")
        st.success(summary)

        st.subheader("🔍 Result")
        if label == "FAKE":
            st.error(f"⚠️ **FAKE** (Confidence: {confidence*100:.1f}%)")
        else:
            st.success(f"✅ **REAL** (Confidence: {confidence*100:.1f}%)")

        st.write(f"Fake Probability: {fake*100:.1f}%")
        st.write(f"Real Probability: {real*100:.1f}%")
```

---

## 🌍 Deploy on Hugging Face (Free)

1. Go to https://huggingface.co/spaces
2. Create **New Space**
3. Choose:
   - SDK: **Streamlit**
   - Hardware: **CPU Basic (Free)**
4. Upload:
   - app.py
   - requirements.txt
5. Wait 2–4 minutes for build

Your app will be live at:

```
https://huggingface.co/spaces/<your-username>/<your-space>
```

---

## 🎉 Done!
Share your link anywhere! 🚀
