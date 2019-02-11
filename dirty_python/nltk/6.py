#%%
# the process of classifying words into their parts of speech - part-of-speech tagging, POS-tagging
# using a tagger
import nltk
from nltk import word_tokenize
# POS tagger attaches a part of speech tag to each word
text = word_tokenize('And now for something completely different')
nltk.pos_tag(text)
# CC - coordinating conjunction, RB - adverbs, IN - preposition, NN - noun, JJ - adj, VBP - verb

# words appearing in the same context
text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
text.similar('woman')
