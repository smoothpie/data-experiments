#%%
import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
from nltk.classify import ClassifierI
from nltk.tokenize import word_tokenize
from statistics import mode
import pickle
from unidecode import unidecode

import sklearn
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB

from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

short_pos = open('/Users/smoothpie/code/data/nltk/sentdex/positive.txt', 'r', encoding='utf-8', errors='replace').read()
short_neg = open('/Users/smoothpie/code/data/nltk/sentdex/negative.txt', 'r', encoding='utf-8', errors='replace').read()

documents = []

for r in short_pos.split('\n'):
  documents.append( (r, 'pos') )

for r in short_neg.split('\n'):
  documents.append( (r, 'neg') )

all_words = []

short_pos_words = word_tokenize(short_pos)
short_neg_words = word_tokenize(short_neg)

for w in short_pos_words:
  all_words.append(w.lower())

for w in short_neg_words:
  all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
# print(all_words.most_common(15))

word_features = [w[0] for w in all_words.most_common(5000)]

def find_features(document):
  words = word_tokenize(document)
  features = {}
  for w in word_features:
    features[w] = (w in words)

  return features

# print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [(find_features(rev), category) for (rev, category) in documents]

random.shuffle(featuresets)

training_set = featuresets[:10000]
testing_set = featuresets[10000:]

# naive bayes
# posterior = prior occurences * likelihood / evidence

classifier = nltk.NaiveBayesClassifier.train(training_set)

# classifier_f = open('naivebayes.pickle', 'rb')
# classifier = pickle.load(classifier_f)
# classifier_f.close()

print("Original Naive Bayes Algo accuracy:", (nltk.classify.accuracy(classifier, testing_set)))
classifier.show_most_informative_features(15)

# save_classifier = open('naivebayes.pickle', 'wb')
# pickle.dump(classifier, save_classifier)
# save_classifier.close()

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB_classifier Algo accuracy:", (nltk.classify.accuracy(MNB_classifier, testing_set)))

# GNB_classifier = SklearnClassifier(GaussianNB())
# GNB_classifier.train(training_set))
# print("MNB_classifier Algo accuracy:", (nltk.classify.accuracy(GNB_classifier, testing_set)))

BNB_classifier = SklearnClassifier(BernoulliNB())
BNB_classifier.train(training_set)
print("BNB_classifier Algo accuracy:", (nltk.classify.accuracy(BNB_classifier, testing_set)))

#

LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression_classifier Algo accuracy:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set)))

SGDClassifier = SklearnClassifier(SGDClassifier())
SGDClassifier.train(training_set)
print("SGDClassifier Algo accuracy:", (nltk.classify.accuracy(SGDClassifier, testing_set)))

SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(training_set)
print("SVC_classifier Algo accuracy:", (nltk.classify.accuracy(SVC_classifier, testing_set)))

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC_classifier Algo accuracy:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set)))

NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print("NuSVC_classifier Algo accuracy:", (nltk.classify.accuracy(NuSVC_classifier, testing_set)))

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

# 
