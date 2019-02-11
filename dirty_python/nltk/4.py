#%%
# lexical resources
# lets define a function  to compute what fraction of words in a text are not in the stopwords list
import nltk

def content_fraction(text):
  stopwords = nltk.corpus.stopwords.words('english')
  content = [w for w in text if w.lower() not in stopwords]
  return len(content) / len(text)

# content_fraction(nltk.corpus.reuters.words())

# a wordlist is useful for solving word puzzles
puzzle_letters = nltk.FreqDist('egivrvonl')
obligatory = 'r'
wordlist = nltk.corpus.words.words()
# [w for w in wordlist if len(w) >=6
#                       and obligatory in w
#                       and nltk.FreqDist(w) <= puzzle_letters]

# names wordlist
names = nltk.corpus.names
male_names = names.words('male.txt')
female_names = names.words('female.txt')
[w for w in male_names if w in female_names]

# its well known that names ending in the letter a are almost always female
cfd = nltk.ConditionalFreqDist(
            (fileid, name[-1])
            for fileid in names.fileids()
            for name in names.words(fileid))

# cfd.plot()

# pronouncing dictionary - designed for use by speech synthesizers
entries = nltk.corpus.cmudict.entries()
len(entries)
# for entry in entries[42371:42379]:
#   print(entry)

# finding rhyming words
syllable = ['N', 'IH0', 'K', 'S']
[word for word, pron in entries if pron[-4:] == syllable]
# the phones contain digits to represent primary stress (1), secondary (2) and no (0)
