#%%
import nltk
from nltk.book import *

# searching text
# a concordance view shows us every occurance of a given word, together with some context
# text1.concordance('monstrous')

# we saw that monstrous occurred in contexts such as the ___ pictures and a ___ size
# what other words appear in a similar range of contexts?
# text1.similar('monstrous')
# text2.similar('monstrous')
# we get different results for different texts
# Austen uses this word quite differently from Melville
# for her it has positive connotations, and sometimes functions as an intensifier like the word very

# the term common_context allows us to examine just the contexts that are shared by two or more words,
# such as monstrous and very
# text2.common_contexts(['monstrous', 'very'])
# it is one thing to automatically detect that a particular word occurs in a text, 
# and to display some words that appear in the same context
# we can also determine the location of a word in the text: how many words from the beginning it appears

# lexical dispersion plot for words in US Presidential Inaugural Addresses
# text4.dispersion_plot(['citizens', 'democracy', 'freedom', 'duties', 'America'])

# lets try generating some random text in the various styles we've just seen
# text3.generate()

# counting vocabulary
# the vocabulary of a text is just the set of tokens that it uses, since it's a set, all duplicates are collapsed together
# len(text3)
# sorted(set(text3))
# len(set(text3))
# so although it has 44764 tokens, the book has only 2789 distinct words, or word types, including punctuation

# now lets calculate a measure of the lexical richness of the text
# the next example shows us that the number of distinct words is just 6% of the total number of words
# or equivalently that each word is used 16 times on average
# len(set(text3)) / len(text3)

# now lets focus on particular words. we can count how often a word occurs in a text
# and compute what % of text is taken up by a specific word
# text3.count('smote')
# 100 * text4.count('the') / len(text4) # lol 6%

def lexical_diversity(text):
  return len(set(text)) / len(text)

def percentage(count, total):
  return 100 * count / total

# frequency distributions
# fdist1 = FreqDist(text1)
# fdist1.most_common(50)
# fdist1['whale']
# only this word is slightly informative, the rest tell nothing about the text.
# what proportion of the text is taken up with such words? 
# fdist1.plot(50, cumulative=True)
# these 50 words account for nearly half the book!
# words that occur once only 
# fdist1.hapaxes()
# too many rare words
# well neither frequent nor infrequent words help, so we need to try sth else

# fine-grained selection of words
# lets look at the long words of a text, these will be more characteristic and informative
# we want to find the words from the vocabulary that are more than 15 characters long
V = set(text1)
long_words = [w for w in V if len(w) > 15]
sorted(long_words)
# notice that the long words in text4 reflect its national focus - constitutionally, transcontinental
# whereas those in text5 reflect its informal content: boooooooooooglyyyyyy and yuuuuuuuuuuuummmmmmmmmmmm

# but those words are often hapaxes and it would be better to find frequently occuring long words
# (helpful since it eliminates frequent short words (the) and infrequent long words)
# finding all words from text5 that are longer than 7 chars and occur more than 7 times
fdist5 = FreqDist(text5)
sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 7)

# collocations and bigrams
# to get a handle on collocations, we start off by extracting from a text a list of word pairs (bigrams)
list(bigrams(['more', 'is', 'said', 'than', 'done']))
# collocations are just frequent bigrams, except that we want to pay more attention to the cases that involve rare words
# text4.collocations()

# counting other things
# we can look at the distribution of word lengths in a text
# [len(w) for w in text1]
fdist = FreqDist(len(w) for w in text1)
fdist.max()
fdist.freq(3)
# from here we see that the most frequent word length is 3, and that these words account for 19% of the words
# although we won't use it now, this can help us understand differences between authors, genres or languages

# language understanding techniques
# word sense disambiguation
# here we want to work out which sense of a word was intended in a given context. Consider those:
# serve: help with food or drink; hold an office; put ball into play
# dish: plate; course of a meal; communications device
# in a sentence containing the phrase: he served the dish, we can detect that both serve and dish are being used with their
# food meanings. or word "by"

# pronoun resolution
# a deeper kind of language understanding is to work out "who did what to whom" - to detect subjects and objects
# in the sentence "the thieves stole the paintings" its easy to tall who performed the actions. but
# - the thieves stole the paintings. they were subsequently sold / they were subsequently caught / found
# computation techniques for tackling this problem include anaphora resolution -
# identifying what a pronoun or noun phrase to
# and semantic role labeling - identifying how a noun phrase relates to the verb

# generating language output, such as question answering and machine translation

# exercises
# text2.dispersion_plot(['Elinor', 'Marianne', 'Edward', 'Willoughby'])
# we can see that Elinor and Marianne are tightly connected and are more important

text5.collocations()
# they wanna chat, listen to music, knows what guys want, describe last nights, don't know and take a long time
list(range(20, 10, -2))


