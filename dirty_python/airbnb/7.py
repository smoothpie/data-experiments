#%%
# thats Chicago airbnb listings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)
sns.set_palette(sns.color_palette("muted"))

df = pd.read_csv("~/code/data/airbnb/better_listings.csv")
pd.set_option('display.max_columns', 100)

# so now lets find a place for us
# oh, we can sort by rating and filter out anything lower than 4
# i also want something cheaper than 100 per night and less than 3 km to city center

df.sort_values('review_scores_value', ascending=False, inplace=True)
df = df.loc[(df['km_to_center'] < 2) & (df['price'] < 80) & (df['number_of_reviews'] >= 5) & (df['room_type'] == 'Entire home/apt')]
df
# also find whats available
# okay 3 of those no longer exist and some have not relevant prices, but there're mostly correct and i've found 3 suitable options