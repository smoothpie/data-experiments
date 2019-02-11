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

# enough with distributions, lets see correlation now

# how different stuff influences price
# df['security_deposit'].corr(df['price']) # 30% - weak
# df['bedrooms'].corr(df['price']) # 41% - well that's sth
# # i should check host_since, host_location, host_is_superhost, room_type, accommodates, guests_included, number_of_reviews, review_scores_rating
# df['accommodates'].corr(df['price']) # 34% - weak
# df['guests_included'].corr(df['price']) # 26% - weak
# df['number_of_reviews'].corr(df['price']) # lol it's negative
# df['review_scores_rating'].corr(df['price']) # 4% only
# okay that's weird

# # how different stuff influences rating
# df['security_deposit'].corr(df['review_scores_rating'])

# x - neighborhood, y - price
# fig = plt.figure(figsize=(20,12))
# plt.xticks(rotation='vertical')
# plt.scatter(df['neighbourhood'].astype(str), df['price'])
# so we see that the most expensive ones are Lakeview, Wicker Park and Loop
# whereas the cheapest are Pullman, Hegewisch, Marquette Park, Cleaning, Roseland, West Pullman and Avalon Park
# but those are really a lot of districts, maybe we have more common ones?

# fig = plt.figure(figsize=(20,12))
# plt.xticks(rotation='vertical')
# plt.scatter(df['neighbourhood_cleansed'].astype(str), df['price']) # not that less

# plt.scatter(df['room_type'].astype(str), df['price'])

df[['security_deposit', 'cleaning_fee', 'extra_people', 'price', 'weekly_price', 'number_of_reviews', 'bedrooms', 'guests_included', 'review_scores_rating']].corr()
# oh okay, we see that number of bedrooms has 62% correlation with cleaning_fee which is pretty logical
# cleaning fee has 54% with price
# bedrooms have 60% with guests_included - again logical

# out of the box solution for statistics
# import pandas_profiling
# pandas_profiling.ProfileReport(df)

# could find the most and least popular neighborhoods

price_groups_order = ['0-25','25-50','50-75','75-100', '100-125','125-150','150-175', '175-200','200+']

# cancellation policy - price category correlation
# fig, axes = plt.subplots(1,2,figsize=(25,5))
# sns.countplot('cancellation_policy', data=df, ax=axes[0], color='blue')
# sns.countplot('cancellation_policy', hue='price_cat', data=df, ax=axes[1], hue_order=price_groups_order)
# nothing too interesting

# bedrooms - price category
# fig, axes = plt.subplots(1,2,figsize=(35,5))
# sns.countplot('bedrooms', data=df, ax=axes[0], color='blue')
# sns.countplot('bedrooms', hue='price_cat', data=df, ax=axes[1], hue_order=price_groups_order)
# so this is clearly obvious, but not that interesting

# neighborhood - price category
# fig, axes = plt.subplots(1,2,figsize=(100,5))
# sns.countplot('neighbourhood', data=df, ax=axes[0], color='blue')
# sns.countplot('neighbourhood', hue='price_cat', data=df, ax=axes[1], hue_order=price_groups_order)
# make it vertical

# create square_feet groups?
# fig, axes = plt.subplots(1,2,figsize=(50,5))
# sns.countplot('square_feet', data=df, ax=axes[0], color='blue')
# sns.countplot('square_feet', hue='price_cat', data=df, ax=axes[1], hue_order=price_groups_order)