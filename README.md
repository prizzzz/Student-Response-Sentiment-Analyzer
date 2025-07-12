
# 🧠 Student Response Sentiment Analyzer

This project focuses on analyzing open-ended student feedback to identify the underlying **sentiment** — positive, neutral, or negative — using **Natural Language Processing (NLP)** and **Machine Learning** techniques.

---

## 📌 Project Overview

Educational institutions often collect qualitative feedback from students, but analyzing open-ended text responses at scale is challenging. This tool automates the process using text classification models, helping educators derive actionable insights from student sentiments.

---

## ⚙️ Features

- ✅ Preprocessing of raw text (tokenization, stopword removal, stemming)
- ✅ Feature extraction using **TF-IDF vectorization**
- ✅ Sentiment classification using ML models:
  - Logistic Regression
  - Support Vector Machine (SVM)
  - Random Forest
- ✅ Model evaluation with accuracy, confusion matrix, and F1 score
- ✅ Easy visualization of sentiment distribution

---

## 🗂️ Folder Structure

```
text-sentiment-analysis-main/
│
├── dataset/                 # Contains student feedback data
├── models/                 # Saved trained ML models
├── MasterDictionary/       # Positive and negative word lists
├── text_sentiment_analysis.py  # Main script
└── README.md               # Project documentation
```

---

## 🧪 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/prizzzz/Student-Response-Sentiment-Analyzer.git
   cd Student-Response-Sentiment-Analyzer
   ```

2. **Install requirements**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the analysis script**
   ```bash
   python text_sentiment_analysis.py
   ```

---

## 🧠 Algorithms Used

- Text preprocessing (NLTK, regular expressions)
- TF-IDF for feature extraction
- Machine Learning models: Logistic Regression, SVM, Random Forest
- Accuracy and F1-score metrics for performance evaluation

---

## 📈 Sample Output

- Sentiment counts (positive, negative, neutral)
- Confusion matrix and classification report
- Sentiment prediction for individual text entries

---

## 👩‍💻 Author

**Priyanka Chougule**  
Final Year B.E. Student – Computer Engineering  
SIES Graduate School of Technology

---

## 📌 Future Enhancements

- Integration of deep learning models (e.g., BERT, LSTM)
- Web-based interface for uploading and analyzing feedback
- Support for multilingual sentiment analysis

---

## 📜 License

This project is open-source and free to use under the [MIT License](LICENSE).
