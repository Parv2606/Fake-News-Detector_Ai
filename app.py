import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Fake News Detector", page_icon="📰", layout="centered")

# ---------------------------------
# Load Models Once
# ---------------------------------
@st.cache_resource
def load_models():
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    detector = pipeline("text-classification", model="mrm8488/bert-tiny-finetuned-fake-news-detection")
    return summarizer, detector

summarizer, detector = load_models()

# ---------------------------------
# Custom CSS UI
# ---------------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(120deg, #4b8bff, #8f41ff);
    color: white;
}
.reportview-container, .block-container {
    background: rgba(255,255,255,0.15) !important;
    backdrop-filter: blur(12px);
    border-radius: 16px;
    padding: 50px;
    color: white !important;
}
textarea, .stTextArea textarea {
    background: rgba(255,255,255,0.7) !important;
    color: black !important;
    border-radius: 12px !important;
    font-size: 16px !important;
}
.stButton>button {
    background: #ffce00 !important;
    color: black !important;
    font-weight: 600;
    border-radius: 12px !important;
    padding: 10px 20px;
}
.stButton>button:hover {
    background: #ffb300 !important;
    transform: scale(1.03);
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------
# UI Layout
# ---------------------------------
st.title("📰 Fake News Detector")
st.write("Analyze news articles for credibility and get an AI-powered summary.")

article = st.text_area("Paste your article here:", placeholder="Type or paste text...")

if st.button("Analyze"):
    if article.strip() == "":
        st.warning("Please enter article text before analyzing.")
    else:
        with st.spinner("Analyzing..."):
            summary = summarizer(article, max_length=120, min_length=30, do_sample=False)[0]['summary_text']
            scores = detector(article, return_all_scores=True)[0]

            fake = real = 0.0
            for item in scores:
                label = item["label"].upper()
                score = float(item["score"])
                if "FAKE" in label: fake = score
                if "REAL" in label or "TRUE" in label: real = score

            label = "FAKE" if fake >= real else "REAL"
            confidence = max(fake, real)

        st.subheader("📌 Summary:")
        st.success(summary)

        st.subheader("🔍 Credibility Result:")
        if label == "FAKE":
            st.error(f"⚠️ This article appears **FAKE** (Confidence: {confidence*100:.1f}%)")
        else:
            st.success(f"✅ This article appears **REAL** (Confidence: {confidence*100:.1f}%)")

        st.write("---")
        st.write(f"**Fake Probability:** {fake*100:.1f}%")
        st.write(f"**Real Probability:** {real*100:.1f}%")

