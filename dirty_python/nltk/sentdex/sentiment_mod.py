#%%
import nltk
import random
# from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
from nltk.classify import ClassifierI
from nltk.tokenize import word_tokenize
from statistics import mode
import pickle

from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

documents_f = open('documents.pickle', 'rb')
documents = pickle.load(documents_f)
documents_f.close()

word_features5k_f = open('word_features5k.pickle', 'rb')
word_features = pickle.load(word_features5k_f)
word_features5k_f.close()

def find_features(document):
  words = word_tokenize(document)
  features = {}
  for w in word_features:
    features[w] = (w in words)

  return features

featuresets = [(find_features(rev), category) for (rev, category) in documents]

random.shuffle(featuresets)

training_set = featuresets[:10000]
testing_set = featuresets[10000:]

open_file = open('originalnaivebayes5k.pickle', 'rb')
classifier = pickle.load(open_file)
open_file.close()

open_file = open('MNB_classifier5k.pickle', 'rb')
MNB_classifier = pickle.load(open_file)
open_file.close()

open_file = open('BNB_classifier5k.pickle', 'rb')
BNB_classifier = pickle.load(open_file)
open_file.close()

open_file = open('LogisticRegression_classifier5k.pickle', 'rb')
LogisticRegression_classifier = pickle.load(open_file)
open_file.close()

open_file = open('SGD_classifier5k.pickle', 'rb')
SGDClassifier = pickle.load(open_file)
open_file.close()

open_file = open('SVC_classifier5k.pickle', 'rb')
SVC_classifier = pickle.load(open_file)
open_file.close()

open_file = open('LinearSVC_classifier5k.pickle', 'rb')
LinearSVC_classifier = pickle.load(open_file)
open_file.close()

open_file = open('NuSVC_classifier5k.pickle', 'rb')
NuSVC_cclassifier = pickle.load(open_file)
open_file.close()

# combining algos with a vote
class VoteClassifier(ClassifierI):
  def __init__(self, *classifiers):
    self._classifiers = classifiers

  def classify(self, features):
    votes = []
    for c in self._classifiers:
      v = c.classify(features)
      votes.append(v)
    return mode(votes)

  def confidence(self, features):
    votes = []
    for c in self._classifiers:
      v = c.classify(features)
      votes.append(v)
    choice_votes = votes.count(mode(votes))
    conf = choice_votes / len(votes)
    return conf

voted_classifier = VoteClassifier(classifier, MNB_classifier, BNB_classifier, LogisticRegression_classifier, SGDClassifier, SVC_classifier, LinearSVC_classifier)
print("voted_classifier Algo accuracy:", (nltk.classify.accuracy(voted_classifier, testing_set)))

print('Classification:', voted_classifier.classify(testing_set[0][0]), 'Confidence %:', voted_classifier.confidence(testing_set[0][0]))

def sentiment(text):
  feats = find_features(text)

  return voted_classifier.classify(feats), voted_classifier.confidence(feats)
