import pandas as pd
import string
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer, PorterStemmer
from collections import Counter

# importing necessary libraries
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt_tab')
stop_words = set(stopwords.words('english'))
punct = list(string.punctuation)
stop_words.update(punct)
lemmatizer = WordNetLemmatizer()

def remove_repLetter(title):
    """This function removes the repeating letters from text"""
    if pd.isna(title) or title == '':
      return ''
    title = re.sub(r'(.)\1{2,}', r'\1', title)
    title = re.sub(r'[^a-zA-Z\s]', '', title)
    return title


def clean_title(title):
    """This function tokenize and lemmetize the text"""
    if pd.isna(title) or title == '':
        return ''
    tokens = word_tokenize(title)
    clean_tokens = []
    for token in tokens:
        token = token.lower()
        if token not in stop_words and token.isalpha():
            lemmatized = lemmatizer.lemmatize(token)
            clean_tokens.append(lemmatized)
    return ' '.join(clean_tokens)


def wordCounter(df):
    """This function counts every words in a text"""
    all_words = [word for sentence in df['clean_text'] for word in word_tokenize(sentence.lower())]
    words_count = Counter(all_words)
    return words_count