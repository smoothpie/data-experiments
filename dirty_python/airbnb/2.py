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

# let's find price range
min_price = df['price'].min() # $0
print('Minimum price per night, $: ', min_price)
max_price = df['price'].max() # $10000 ?
print('Maximum price per night, $: ', max_price)
# this seems extreme. lets draw a distribution graph
df['price'].value_counts()
# wee see that there is one value with $10000 which is an obvious outlier. and all prices generally go from 0 to $1500.

# it becomes hard to comment on single values of a variable which is continuous in nature and can be having
# too many values. So categorizing it comes to rescue
df['price_cat'] = 0
df.loc[df.price <= 25, 'price_cat'] = "0-25"
df.loc[(df.price > 25) & (df.price <= 50), 'price_cat'] = "25-50"
df.loc[(df.price > 50) & (df.price <= 75), 'price_cat'] = "50-75"
df.loc[(df.price > 75) & (df.price <= 100), 'price_cat'] = "75-100"
df.loc[(df.price > 100) & (df.price <= 125), 'price_cat'] = "100-125"
df.loc[(df.price > 125) & (df.price <= 150), 'price_cat'] = "125-150"
df.loc[(df.price > 150) & (df.price <= 175), 'price_cat'] = "150-175"
df.loc[(df.price > 175) & (df.price <= 200), 'price_cat'] = "175-200"
df.loc[df.price > 200, 'price_cat'] = "200+"
price_groups_order = ['0-25','25-50','50-75','75-100', '100-125','125-150','150-175', '175-200','200+']
df['price_cat'].value_counts()
plt.figure(figsize=(8,4))
# print('Price per night distribution for all listings')
# print(sns.countplot('price_cat', data=df, color='blue', order=price_groups_order))
# so we see that most flats lie in $75-100 category. but this is for all of them.
# lets find it for private rooms and entire home with one bedroom
private_room = df.loc[(df.room_type == 'Private room') & (df.bedrooms == 1)]
entire_home = df.loc[(df.room_type == 'Entire home/apt') & (df.bedrooms == 1)]

# print('Price per night distribution for private rooms with one bedroom')
# print(sns.countplot('price_cat', data=private_room, color='blue', order=price_groups_order))
# so private one bedroom is mostly 25-50
# print('Price per night distribution for entire homes with one bedroom')
# print(sns.countplot('price_cat', data=entire_home, color='blue', order=price_groups_order))
# so entire home one bedroom is mostly 75-100

# lets see this info combined
fig, axes = plt.subplots(1,2,figsize=(18,5))
sns.countplot('room_type', data=df, ax=axes[0], color='blue')
sns.countplot('room_type', hue='price_cat', data=df, ax=axes[1], hue_order=price_groups_order)
# ah so here we see sth which is obvious, private room mostly lie in 25-50 range, entire home - 75 - 100
# hm weird why do we have this high 200+
# and shared room is kist cheaper with each price increase

pd.crosstab([df.price],[df.room_type],margins=True).style.background_gradient(cmap='summer_r')
# so here we see that almost a half of shared rooms cost 25$
# i mean i don't know if this is any valuable

# let's save it to our better_listings file
df.to_csv('better_listings.csv', index=False)