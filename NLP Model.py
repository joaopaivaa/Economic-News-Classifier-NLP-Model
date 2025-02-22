import re
import nltk
from nltk.corpus import stopwords
import pandas as pd
import numpy as np

nltk.download('stopwords')
stop_words = set(stopwords.words('portuguese'))

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

df = pd.read_csv('Brazilian News Database.csv', delimiter=';', encoding="Windows-1252")
df = df[df['status'] != 'Neutral']

df_train = df.iloc[0:round(0.8*len(df))]

df_test = df.iloc[round(0.8*len(df)):]

train_texts = df_train["text"]
train_labels = np.array(df_train["status"])

test_texts = df_test["text"]
test_labels = np.array(df_test["status"])

train_texts = [preprocess_text(text) for text in train_texts]
test_texts = [preprocess_text(text) for text in test_texts]

train_texts_splitted = []
for text in train_texts:
    train_texts_splitted = text.split(' ') + train_texts_splitted
#train_texts_splitted = set(train_texts_splitted)
train_texts_splitted = [word for word in train_texts_splitted if not word.isdigit()]
#train_texts_splitted = [word for word in train_texts_splitted if len(word)>=5]

test_texts_splitted = []
for text in train_texts:
    test_texts_splitted = text.split(' ') + test_texts_splitted
#test_texts_splitted = set(test_texts_splitted)
test_texts_splitted = [word for word in test_texts_splitted if not word.isdigit()]
#test_texts_splitted = [word for word in test_texts_splitted if len(word)>=5]

pass