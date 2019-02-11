#%%
import sys
from os.path import dirname
textFileFolder = "/Users/smoothpie/code/data/nltk/sentdex"
sys.path.append(textFileFolder)

# okay there's gottaa be a normal way of doing this

import sentiment_mod as s

print(s.sentiment("This movie was awesome! The acting was great, plot was wonderful, and there were pythons...so yea!"))
print(s.sentiment("This movie was utter junk. There were absolutely 0 pythons. I dont see what the point was at all. Horrible movie, 0/10"))