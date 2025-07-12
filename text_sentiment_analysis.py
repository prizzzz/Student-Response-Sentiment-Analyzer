import pandas as pd
import nltk
import re
import chardet
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

nltk.download('punkt')

#input file
df = pd.read_excel('Event Registration (Responses)New.xlsx')

# Questions
questions = {
    "How would you describe your overall satisfaction with the college campus environment? What aspects do you find most supportive or lacking?": "Q1",
    "Share your thoughts on the quality of campus facilities, such as the library, labs, and sports areas. How well do they meet your needs as a student, and what could be improved?": "Q2",
    "Reflect on your social life on campus. Do you feel there are enough opportunities for making connections and participating in extracurricular activities? Why or why not?": "Q3",
    "Overall, how has your experience on campus affected your personal growth? Are there particular aspects of campus life that have positively or negatively shaped your journey?": "Q4"
}

#stop list
stop_list = []
for files in os.listdir('./StopWords'):
    filename = './StopWords/' + files

    with open(filename, 'rb') as file:
        raw_data = file.read(1000) 
        result = chardet.detect(raw_data)
        encoding = result['encoding']

    with open(filename, 'r', encoding=encoding) as file:
        stop_list.extend(file.read().splitlines())

# Load positive and negative words with encoding detection
def load_word_list(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            words = f.read().splitlines()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='ISO-8859-1') as f:
            words = f.read().splitlines()

    return [word.lower().strip() for word in words if word] 

# Load positive and negative words
pos = load_word_list("./MasterDictionary/positive-words.txt")
neg = load_word_list("./MasterDictionary/negative-words.txt")

analyzer = SentimentIntensityAnalyzer()

#clean and process text
def clean_text(text):
    hyphenated_pattern = re.compile(r'\b\w+-\w+\b') 
    hyphenated_words = hyphenated_pattern.findall(text)

    text = re.sub(r'[^\w\s-]', '', text)
    text = text.lower()

    for word in stop_list:
        if word.lower() in pos or word.lower() in neg:
            continue 
        text = re.sub(r'\b' + re.escape(word.lower()) + r'\b', '', text)

    for word in hyphenated_words:
        text = text.replace(word.lower().replace('-', ' '), word.lower())
    
    text = re.sub(r'\s+', ' ', text).strip()

    print(f"Cleaned Text: {text}")

    return text

#sentiment analysis using VADER
def sentiment_analysis(text):
    vader_scores = analyzer.polarity_scores(text)

    pos_words = [word for word in text.split() if word.lower() in pos]
    neg_words = [word for word in text.split() if word.lower() in neg]
    
    pos_score = len(pos_words)
    neg_score = len(neg_words)

    # Print positive and negative words
    print(f"Positive Words: {pos_words}")
    print(f"Negative Words: {neg_words}")

    return {
        'POSITIVE SCORE': round(pos_score, 4), 
        'NEGATIVE SCORE': round(neg_score, 4), 
        'POLARITY SCORE': round(vader_scores['compound'], 4),  
        'SUBJECTIVITY SCORE': round((pos_score + neg_score) / max(len(text.split()), 1), 4), 
        'AVG SENTENCE LENGTH': round(len(text.split()) / max(len(nltk.sent_tokenize(text)), 1), 4)
    }


for i in range(len(df)):
    for question, short_label in questions.items():
        response = df.loc[i, question] 
        if pd.isna(response):
            continue 
        
        cleaned_response = clean_text(response)  
        metrics = sentiment_analysis(cleaned_response)  

        for metric, value in metrics.items():
            df.loc[i, f'{short_label} - {metric}'] = value

if 'Timestamp' in df.columns:
    df = df.drop(columns=['Timestamp'])


df.to_excel('Sentiment_Analysis_Output_1.xlsx', index=False)

print("Sentiment analysis completed and the existing Excel sheet has been updated.")










