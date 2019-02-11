#%%
# wordnet - semantically-oriented dictionary of english
# senses and synonyms
from nltk.corpus import wordnet as wn
wn.synsets('motorcar')
wn.synset('car.n.01').lemma_names()
wn.synset('car.n.01').definition()
wn.synset('car.n.01').examples()

# unlike the word motorcar, which is unambiguous and has one synset, the word car is ambiguous, having 5
wn.synsets('car')
for synset in wn.synsets('car'):
  print(synset.lemma_names())

wn.lemmas('car')

# wn.synsets('dish')
# wn.synset('dish.n.05').lemma_names()
# wn.lemmas('dish')

# we can also look at types of car
motorcar = wn.synset('car.n.01')
types_of_motorcar = motorcar.hyponyms()
types_of_motorcar[0]
# sorted(lemma.name() for synset in types_of_motorcar for lemma in synset.lemmas())
# or up the hierarchy
motorcar.hypernyms()

# or parts of
wn.synset('tree.n.01').part_meronyms()
wn.synset('tree.n.01').substance_meronyms()
# or what it's a part of
wn.synset('tree.n.01').member_holonyms()

# relationship between verbs
wn.synset('walk.v.01').entailments()
wn.synset('eat.v.01').entailments()

# antonyms
wn.lemma('supply.n.02.supply').antonyms()
wn.lemma('staccato.r.01.staccato').antonyms()