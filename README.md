# 🕵️‍♂️ AI Fake Review Detection System

An AI-powered web app to detect fake reviews from Google Play Store apps using Meta’s LLaMA model (via Groq API) combined with a TF-IDF + Random Forest classifier. It helps users identify app trustworthiness based on review analysis.

---

## 🚀 Features

- 🔍 Scrapes reviews from Google Play Store apps
- 🧠 Detects fake/genuine reviews using:
  - Machine Learning (TF-IDF + Random Forest)
  - Meta LLaMA model via Groq API
- 📊 Displays:
  - Total, fake & genuine review counts and percentages
  - Accuracy of the ML model
  - Final recommendation: Try or Avoid
- 🌐 Flask-based web app with a simple UI

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, Bootstrap
- **Backend:** Python (Flask)
- **ML:** scikit-learn, pandas, numpy
- **AI Integration:** Meta LLaMA via Groq API
- **Scraping:** `google-play-scraper` or BeautifulSoup

---

## 📁 Project Structure

