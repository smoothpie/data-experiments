#%%
# thats Chicago airbnb listings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)
sns.set_palette(sns.color_palette("muted"))

df = pd.read_csv("~/code/data/airbnb/listings.csv")
pd.set_option('display.max_columns', 100)

# initial thoughts
# reviews per month are important
# we should find price range
# weekly and monthly price - percentage of hosts offering discounts
# security deposit - its range and how it influences and its correlation with price
# cleaning fee span and how it influences bookings, oh but we don't have bookings data
# extra people fee distribution
# we can sort data by review scores
# see percentages of different cancellation policies, offered experiences, instant bookable, is business travel ready
# i think would be good if we had amount of bookings and track what influences this number
# how neighborhood influences reviews and price
# how host_response_time and host_response_rate influences reviews
# room type (room, entire) influences price
# number of accommodates can influence price
# min/max nights distribution
# what people rate the least and the highest
# i would also analyse the amount of images and its influence, but i see only one main image per listing here

# i am also able to find available ones for my needs, filter music related
# also, in future, compare prices through cities/states (one-bedroom)

# ------------

# okay so lets calculate the total of existing listings
# len(df) # 7594 records of places in Chicago

# oh damn, nothing works because they have this dollar sign in front! lets get rid of them!
cols = ['price', 'weekly_price', 'monthly_price', 'security_deposit', 'cleaning_fee', 'extra_people']
replace_dict = {'\$': '', ',': ''}
for col in cols:
  df[col] = df[col].str.replace('$', '')
  df[col] = df[col].str.replace(',', '').astype(float)
# df[cols] = df[cols].replace({'\$': '', ',': ''}, regex=True) # that's a pretty slow method, but will do for now

# other preprocessing here

# lets save our improved dataset to a file
df.to_csv('better_listings.csv', index=False)