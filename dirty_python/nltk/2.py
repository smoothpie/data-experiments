#%%
# accessing text corpora
# a text corpus is a large body of text
from nltk.corpus import gutenberg
gutenberg.fileids()

emma = gutenberg.words('austen-emma.txt')

# for fileid in gutenberg.fileids():
#   num_chars = len(gutenberg.raw(fileid))
#   num_words = len(gutenberg.words(fileid))
#   num_sents = len(gutenberg.sents(fileid))
#   num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
#   print(round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid)
# this displays average word length, average sentence length and the number of times each vocabulary item appears on average

# raw() function gives us the contents of the file without any linguistic processing

# web and chat text
# although gutenberg contains thousands of books, we also need sth less formal
from nltk.corpus import webtext 

# for fileid in webtext.fileids():
#   print(fileid, webtext.raw(fileid)[:65], '...')

# from nltk.corpus import nps_chat
# chatroom = nps_chat.posts('10-19-20s_706posts.xml')
# chatroom[123]

# brown corpus
from nltk.corpus import brown
brown.categories()

brown.words(categories='news')
brown.words(fileids=['cg22'])
brown.sents(categories=['news', 'editorial', 'reviews'])

# convenient for studying genre differences (stylistics)
# lets compare genres in their usage of modal verbs
# news_text = brown.words(categories='news')
# fdist = nltk.FreqDist(w.lower() for w in news_text)
# modals = ['can', 'could', 'may', 'might', 'must', 'will']
# for m in modals:
#   print(m + ':', fdist[m], end=' ')
# end=' ' is for putting output on a single line
# mystery_text = brown.words(categories='mystery')
# fdist = nltk.FreqDist(w.lower() for w in mystery_text)
# modals = ['can', 'could', 'may', 'might', 'must', 'will']
# for m in modals:
#   print(m + ':', fdist[m], end=' ')
# oh mystery has much less will than news (25 vs 389)

# cfd = nltk.ConditionalFreqDist(
#            (genre, word)
#            for genre in brown.categories()
#            for word in brown.words(categories=genre))
# genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
# modals = [''can', 'could', 'may', 'might', 'must', 'will'']
# cfd.tabulate(conditions=genres, samples=modals)

# reuters corpus - news documents
from nltk.corpus import reuters
# categories of one news piece
# reuters.categories('training/9865')
# or see what news cover the topic
# reuters.fileids('barley')

# corpora in other languages
from nltk.corpus import udhr
# cumulative word length distribution
# languages = ['English', 'German_Deutsch',
#      'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
# cfd = nltk.ConditionalFreqDist(
#   (lang, len(word))
#   for lang in languages
#   for word in udhr.words(lang + '-Latin1'))

# cfd.plot(cumulative=True)

# loading your own corpus
from nltk.corpus import PlaintextCorpusReader
corpus_root = ''
wordlists = PlaintextCorpusReader(corpus_root, '.*')
wordlists.fileids()

