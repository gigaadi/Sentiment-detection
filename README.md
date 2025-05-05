# 🎯 YouTube Comment Sentiment Analyzer

A **Streamlit-based** web app that performs **sentiment analysis** on YouTube video comments and user-entered text using **Natural Language Processing (NLP)**. This project helps educators and content creators gain insights into audience feedback on educational course videos.

---

## 🔍 Features

- 📺 **YouTube Video Analysis**  
  Enter any YouTube course video URL and the app will:
  - Extract up to 100 English comments using the YouTube Data API
  - Perform sentiment analysis (positive, negative, neutral)
  - Display an overall sentiment summary

- 💬 **Single Comment Analyzer**  
  Type any text comment and get an instant sentiment classification.

- 🌐 **Language Detection**  
  Ensures only English comments are analyzed using `langdetect`.

- 🧠 **NLP with TextBlob**  
  Uses `TextBlob` for calculating comment polarity (sentiment strength).

---

## 🛠️ Tech Stack

- **Frontend/UI:** Streamlit  
- **NLP:** TextBlob  
- **Language Detection:** langdetect  
- **YouTube API:** Google API Client  
- **Programming Language:** Python  

---

