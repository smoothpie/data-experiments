#%%
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize('cats'))
print(lemmatizer.lemmatize('geese'))
print(lemmatizer.lemmatize('rocks'))

print(lemmatizer.lemmatize('better', pos='a'))
print(lemmatizer.lemmatize('best', pos='a'))