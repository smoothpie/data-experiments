#%%
import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
from nltk.classify import ClassifierI
from nltk.tokenize import word_tokenize
from statistics import mode
import pickle

import sklearn
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB

from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

short_pos = open('/Users/smoothpie/code/data/nltk/sentdex/positive.txt', 'r', encoding='utf-8', errors='replace').read()
short_neg = open('/Users/smoothpie/code/data/nltk/sentdex/negative.txt', 'r', encoding='utf-8', errors='replace').read()

documents = []

# j is adject, r is adverb, and v is verb
# allowed_word_types = ['J', 'R', 'V']
allowed_word_types = ['J']
all_words = []

for p in short_pos.split('\n'):
  documents.append( (p, 'pos') )
  words = word_tokenize(p)
  pos = nltk.pos_tag(words)
  for w in pos:
    if w[1][0] in allowed_word_types:
      all_words.append(w[0].lower())

for p in short_neg.split('\n'):
  documents.append( (p, 'neg') )
  words = word_tokenize(p)
  pos = nltk.pos_tag(words)
  for w in pos:
    if w[1][0] in allowed_word_types:
      all_words.append(w[0].lower())

save_documents = open('documents.pickle', 'wb')
pickle.dump(documents, save_documents)
save_documents.close()

all_words = nltk.FreqDist(all_words)
# print(all_words.most_common(15))

word_features = [w[0] for w in all_words.most_common(5000)]

save_word_features = open('word_features5k.pickle', 'wb')
pickle.dump(word_features, save_word_features)
save_word_features.close()

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

save_classifier = open('originalnaivebayes5k.pickle', 'wb')
pickle.dump(classifier, save_classifier)
save_classifier.close()

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB_classifier Algo accuracy:", (nltk.classify.accuracy(MNB_classifier, testing_set)))

save_classifier = open('MNB_classifier5k.pickle', 'wb')
pickle.dump(MNB_classifier, save_classifier)
save_classifier.close()

BNB_classifier = SklearnClassifier(BernoulliNB())
BNB_classifier.train(training_set)
print("BNB_classifier Algo accuracy:", (nltk.classify.accuracy(BNB_classifier, testing_set)))

save_classifier = open('BNB_classifier5k.pickle', 'wb')
pickle.dump(BNB_classifier, save_classifier)
save_classifier.close()

LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression_classifier Algo accuracy:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set)))

save_classifier = open('LogisticRegression_classifier5k.pickle', 'wb')
pickle.dump(LogisticRegression_classifier, save_classifier)
save_classifier.close()

SGDClassifier = SklearnClassifier(SGDClassifier())
SGDClassifier.train(training_set)
print("SGDClassifier Algo accuracy:", (nltk.classify.accuracy(SGDClassifier, testing_set)))

save_classifier = open('SGD_classifier5k.pickle', 'wb')
pickle.dump(SGDClassifier, save_classifier)
save_classifier.close()

SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(training_set)
print("SVC_classifier Algo accuracy:", (nltk.classify.accuracy(SVC_classifier, testing_set)))

save_classifier = open('SVC_classifier5k.pickle', 'wb')
pickle.dump(SVC_classifier, save_classifier)
save_classifier.close()

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC_classifier Algo accuracy:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set)))

save_classifier = open('LinearSVC_classifier5k.pickle', 'wb')
pickle.dump(LinearSVC_classifier, save_classifier)
save_classifier.close()

NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print("NuSVC_classifier Algo accuracy:", (nltk.classify.accuracy(NuSVC_classifier, testing_set)))

save_classifier = open('NuSVC_classifier5k.pickle', 'wb')
pickle.dump(NuSVC_classifier, save_classifier)
save_classifier.close()

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

  return voted_classifier.classify(feats)
