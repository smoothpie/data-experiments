#%%
# conditional frequency distributions

# when the texts of a corpus are divided into several categories, we can maintain separate frequency distributions for each
# the condition will often be the category

# a frequency distribution counts observable events, such as the appearance of words in a text
# a conditional FD needs to pair each event with a condition
# so instead of processing a sequence of words (1), we have to provess a sequence of pairs (2)
# text = ['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', ...] [1]
# pairs = [('news', 'The'), ('news', 'Fulton'), ('news', 'County'), ...] [2]

# counting words by genre
from nltk.corpus import brown
genre_word = [(genre, word)
              for genre in ['news', 'romance']
              for word in brown.words(categories=genre)]

len(genre_word)
genre_word[:4]
genre_word[-4:]

# we can now use this list of pairs to create a CFD
cfd = nltk.ConditionalFreqDist(genre_word)
cfd.conditions()
cfd['news'].most_common(20)
cfd['romance'].most_common(20)
cfd['romance']['could']

# tabulation
# from nltk.corpus import udhr
# languages = ['Chickasaw', 'English', 'German_Deutsch',
#      'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
# cfd = nltk.ConditionalFreqDist(
#   (lang, len(word))
#   for lang in languages
#   for word in udhr.words(lang + '-Latin1'))
# cfd.tabulate(conditions=['English', 'German_Deutsch'],
#               samples=range(10), cumulative=True)

# cfd.plot(conditions=['news', 'romance'],
#             samples=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], cumulative=True)

# cfd.tabulate(conditions=['news', 'romance'],
#             samples=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], cumulative=True)
# so the closer the end of the week, the more it's popular both in news and romance lol

# generating random text with bigrams
def generate_model(cfdist, word, num=15):
  for i in range(num):
    print(word, end=' ')
    word = cfdist[word].max()

text = nltk.corpus.genesis.words('english-kjv.txt')
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)
cfd['living']
generate_model(cfd, 'living')
