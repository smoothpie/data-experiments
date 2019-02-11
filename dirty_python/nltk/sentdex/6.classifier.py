#%%
import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
from nltk.classify import ClassifierI
from statistics import mode
import pickle

import sklearn
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB

from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

documents = [(list(movie_reviews.words(fileid)), category)
              for category in movie_reviews.categories()
              for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = []
for w in movie_reviews.words():
  all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
# print(all_words.most_common(15))

word_features = [w[0] for w in all_words.most_common(3000)]

def find_features(document):
  words = set(document)
  features = {}
  for w in word_features:
    features[w] = (w in words)

  return features

# print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [(find_features(rev), category) for (rev, category) in documents]

training_set = featuresets[:1900]
testing_set = featuresets[1900:]

# naive bayes
# posterior = prior occurences * likelihood / evidence

# classifier = nltk.NaiveBayesClassifier.train(training_set)

classifier_f = open('naivebayes.pickle', 'rb')
classifier = pickle.load(classifier_f)
classifier_f.close()

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
