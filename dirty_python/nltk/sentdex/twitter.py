#%%
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sys
from os.path import dirname
textFileFolder = "/Users/smoothpie/code/data/nltk/sentdex"
sys.path.append(textFileFolder)

import sentiment_mod as s

#consumer key, consumer secret, access token, access secret.
ckey="5g0d38MDIYGBYt5AVztHHX0Nz"
csecret="2Wcrh5IWiVvq7rfoBOX4mgXLqzLvegvf1Vf8hv6lapw0m6lkbg"
atoken="2836957199-Kzug2ujhyBNSOMWv4zaOTagiFhE83s8wOzo22ZZ"
asecret="npFJIQ86PFxAbHdLaBCvCEARjz0dkUMVX3Geyve4rTBbG"

class listener(StreamListener):

  def on_data(self, data):
    all_data = json.loads(data)
    
    tweet = all_data["text"]
    sentiment_value, confidence = s.sentiment(tweet)

    print((tweet, sentiment_value, confidence))

    if confidence*100 >= 80:
      output = open('twitter-out.txt', 'a')
      output.write(sentiment_value)
      output.write('\n')
      output.close()

    return True

  def on_error(self, status):
    print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["iphone"])