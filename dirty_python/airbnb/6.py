#%%
# thats Chicago airbnb listings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)
sns.set_palette(sns.color_palette("muted"))

df = pd.read_csv("~/code/data/airbnb/better_listings.csv")
pd.set_option('display.max_columns', 100)

# text analysis
# lets remove all the noise from here
import nltk
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer

# lets do some preprocessing first

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

df['description'].fillna('', inplace=True)

df['description'] = df['description'].apply(lambda x: preprocess(x))
all_words = []

# now we can look at some description patterns

# for d in list(df['description']):
#   all_words.extend(word_tokenize(d))

# all_words = nltk.FreqDist(all_words)
# all_words.most_common(70)

# okay this was somehow an alternative way of doing this
# np.set_printoptions(threshold=np.inf)
# dict(df['description'].str.split(expand=True).stack().value_counts()[:200])

# okay, so from this we can say only that frequent words, apart from the most obvious ones are 
# 'park', 'space', 'access', 'restaurants', 'walk', 'neighborhood', 'private', 'downtown', 'street', 'parking',
# 'minutes', 'great', 'train', 'distance', 'bars', 'free', 'close', 'queen', 'TV', 'large', 'bus', 'quiet', 'comfortable',
# 'coffee', 'location'
# so this was top 25 words in description

# all_words = nltk.Text(all_words)
# all_words.collocations()
# one of the popular collocations are: living room, walking distance, Wrigley Field, washer dryer, Logan Square,
# public transportation, Wicker Park, minute walk, Blue Line, street parking, size bed, Lincoln Park, Lake Michigan
# Magnificent Mile, restaurants bars, business travelers
# so we can see that collocations are mostly connected with location, city highlights, bed size, availability of
# transport and restaurants and possibilities for business travelers.

# lets explore name trends
# df['name'].fillna('', inplace=True)
# df['name'] = df['name'].apply(lambda x: preprocess(x))
# all_words = []

# for d in list(df['name']):
#   all_words.extend(word_tokenize(d))

# all_words = nltk.FreqDist(all_words)
# all_words.most_common(50)

# park, chicago, private, room, cozy, apartment, bedroom, square, spacious, Logan - 10
# Wrigley, Wicker, Condo, Home, Lincoln, Downtown, Modern, Studio, Luxury, Loop - 20
# Town, Lakeview, Loft, 2BR, West - 25
# so it's again, park, privacy, coziness, bedrooms, space, modern, luxury and locations

# all_words = nltk.Text(all_words)
# all_words.collocations()
# so all of them name some spotlights plus Private Room and Free Parking

# neighborhood overview
# df['neighborhood_overview'].fillna('', inplace=True)
# df['neighborhood_overview'] = df['neighborhood_overview'].apply(lambda x: preprocess(x))

# for d in list(df['neighborhood_overview']):
#   all_words.extend(word_tokenize(d))

# all_words = nltk.FreqDist(all_words)
# all_words.most_common(50)

# Park, restaurants, bars, walking, distance, downtown, minutes, great, shops, street - 10

# all_words = nltk.Text(all_words)
# all_words.collocations()

# walking distance, all the sights, coffee shops, public transportation, restaurants bars

# df['interaction'].fillna('', inplace=True)
# df['interaction'] = df['interaction'].apply(lambda x: preprocess(x))

# for d in list(df['interaction']):
#   all_words.extend(word_tokenize(d))

# all_words = nltk.FreqDist(all_words)
# all_words.most_common(50)
# available, questions, text, phone, help, happy, call, email, recommendations, love

# all_words = nltk.Text(all_words)
# all_words.collocations()
# answer questions, new people, Fitness Enthusiast lol, outdoors gym, enjoying outdoors, playing sports, cool guy

# df['house_rules'].fillna('', inplace=True)
# df['house_rules'] = df['house_rules'].apply(lambda x: preprocess(x))

# for d in list(df['house_rules']):
#   all_words.extend(word_tokenize(d))

# all_words = nltk.Text(all_words)
# all_words.collocations()
# loud music, security deposit, check time, quiet hours, disturbances reported, law prohibits, overnight guests
# noise disturbances, cancel withing
# so basically noise, security, check in times, cancellation policy and overnight guests