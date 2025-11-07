---
title: Fake News Detector
emoji: 📰
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: "1.32.0"
app_file: app.py
pinned: false
---

# 📰 Fake News Detector — Streamlit App

A modern and interactive **Fake News Detection** tool powered by **Transformers** and **Streamlit**.  
Paste any news content or article, and the app will:

✅ Generate a **summary** of the text  
✅ Detect if the news is **REAL** or **FAKE**  
✅ Show **confidence probability scores**  
✅ Provide a clean, aesthetic UI for easy use  

---

## 🎯 Live Demo (Hugging Face Spaces)

👉 https://huggingface.co/spaces/Parv2608/fake-news-detector

---

## 🧠 Models Used

| Component | Model | Purpose |
|----------|--------|---------|
| Summarization | `sshleifer/distilbart-cnn-12-6` | Generates a concise summary |
| Fake News Detection | `mrm8488/bert-tiny-finetuned-fake-news-detection` | Classifies text as FAKE or REAL |

---

## 💡 Features

- Simple copy/paste usage
- Accurate & lightweight model
- Glassmorphism modern UI
- Runs **Free Forever** on Hugging Face Spaces
- Mobile & Desktop friendly

---

## 📦 Installation (Local Use)

```bash
pip install streamlit transformers sentencepiece accelerate
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

Run the app:

```bash
streamlit run app.py
```

---

## 🚀 Deployment on Hugging Face Spaces

1. Go to: https://huggingface.co/spaces
2. **New Space → Streamlit → CPU Basic**
3. Upload:
   - `app.py`
   - `requirements.txt`
   - `README.md`
4. Wait 2–4 minutes for auto-build

Your app is now **online & never sleeps** 🎉

---

## 📝 requirements.txt

```
streamlit
transformers==4.39.3
sentencepiece
accelerate
torch==2.2.1 --index-url https://download.pytorch.org/whl/cpu
```

---

## 🤝 Contributing

Pull requests and improvements are always welcome!  
Feel free to fork the repository and enhance the project.

---

## 📜 License

This project is released under the **MIT License**.

---

### ⭐ If you like this project, give it a star on GitHub & share your deployment!
