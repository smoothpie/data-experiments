#%%
# thats Chicago airbnb reviews
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)
sns.set_palette(sns.color_palette("muted"))

df = pd.read_csv("~/code/data/airbnb/reviews.csv")
pd.set_option('display.max_columns', 100)
df.head()

len(df)
# 268612 reviews

import nltk
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer

stopwords = stopwords.words('english')
lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()

def preprocess(text):
  tokenizer = RegexpTokenizer(r'\w+')
  tokens = tokenizer.tokenize(text)
  for t in tokens:
    for w in word_tokenize(t):
      w = lemmatizer.lemmatize(w.lower(), pos='v')
  filtered_words = filter(lambda token: token.lower() not in stopwords, tokens)
  return " ".join(filtered_words)

df['comments'].fillna('', inplace=True)
# df['comments'] = df['comments'].apply(lambda x: preprocess(x))
# all_words = []

# for d in list(df['comments']):
#   all_words.extend(word_tokenize(d))

# all_words = nltk.FreqDist(all_words)
# all_words.most_common(50)
# location, clean, host, comfortable, recommend, easy, neighborhood, space, restaurants, area
# walk, downtown, quiet, helpful, friendly, parking
# so people cherish location, cleanliness, comfort, low noise level, parking, places to eat and communication with host

# all_words = nltk.Text(all_words)
# all_words.collocations()
# walking distance, highly recommend, public transportation, definitely stay, great location, blue line, come back
# everything needed, quick respond, Logan Square, Wicker Park, great host
# so location, transport, quick response and great host

import sys
from os.path import dirname
textFileFolder = "/Users/smoothpie/code/data/nltk/sentdex"
sys.path.append(textFileFolder)

# okay there's gottaa be a normal way of doing this

# import sentiment_mod as s

df = df[:5000]
# df['sentiment'] = ''
# df['sentiment'] = df.apply(lambda row: s.sentiment(row.comments), axis=1)
# so well okay, we can do sentiment analysis here, but i don't see what it can give us, since we have rating system

