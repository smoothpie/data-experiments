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

# lets find distance to center and add it to our dataframe, this will be helpful in future

center_latitude = 41.8827
center_longitude = -87.6226

# formula to find distance in km
def haversine(lat1, lon1, lat2, lon2):
  R = 6367

  dLat = np.radians(lat2 - lat1)
  dLon = np.radians(lon2 - lon1)
  lat1 = np.radians(lat1)
  lat2 = np.radians(lat2)

  a = np.sin(dLat/2)**2 + np.cos(lat1)*np.cos(lat2)*np.sin(dLon/2)**2
  c = 2*np.arcsin(np.sqrt(a))

  return R * c

df['km_to_center'] = 0
df['km_to_center'] = df.apply(lambda row: haversine(row.latitude, row.longitude, center_latitude, center_longitude), axis=1)

# now lets find the distribution
df['km_to_center'].value_counts()
df['km_to_center_cat'] = 0
df.loc[df.km_to_center <= 2, 'km_to_center_cat'] = "<2"
df.loc[(df.km_to_center > 2) & (df.km_to_center <= 5), 'km_to_center_cat'] = "2-5"
df.loc[(df.km_to_center > 5) & (df.km_to_center <= 10), 'km_to_center_cat'] = "5-10"
df.loc[df.km_to_center > 10, 'km_to_center_cat'] = "10+"
distance_groups_order = ['<2','2-5','5-10','10+']
df['km_to_center_cat'].value_counts()

price_groups_order = ['0-25','25-50','50-75','75-100', '100-125','125-150','150-175', '175-200','200+']

fig, axes = plt.subplots(1,2,figsize=(25,5))
sns.countplot('km_to_center_cat', data=df, ax=axes[0], color='blue', order=distance_groups_order)
sns.countplot('km_to_center_cat', hue='price_cat', data=df, ax=axes[1], order=distance_groups_order, hue_order=price_groups_order)

df['km_to_center'].corr(df['price'])
# okay we've found that it doesn't matter that much if i'm correct, correlation is slightly negative
# which seems correct - the bigger the distance, the lower the price

# let's save it to our better_listings file
df.to_csv('better_listings.csv', index=False)