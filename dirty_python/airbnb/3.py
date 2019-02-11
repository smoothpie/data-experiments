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

# all the other distributions

# percentage of listings that offer discounts for longer stay
print('Percentage of hosts who offer weekly discounts')
print(len(df.loc[df['weekly_price'] < (df['price'] * 7)]) / len(df) * 100) # only 6% hosts offer weekly discounts
print('Percentage of hosts who dont specify discount info')
print(len(df.loc[df['weekly_price'].isnull()]) / len(df) * 100) # and 91% don't specify this info

print('Percentage of hosts who offer monthly discounts')
print(len(df.loc[df['monthly_price'] < (df['price'] * 7)]) / len(df) * 100) # only 0,1% hosts offer monthly discounts, that like nothing
print('Percentage of hosts who dont specify discount info')
print(len(df.loc[df['monthly_price'].isnull()]) / len(df) * 100) # and 91% don't specify this info

# cleaning_fee distribution
print('Percentage of hosts who dont charge cleaning fee')
print(len(df.loc[df['cleaning_fee'] == 0]) / len(df) * 100) # only 4% of listings don't charge cleaning fee

# percentage of listings without security deposit
print('Percentage of hosts who dont charge security deposit')
print(len(df.loc[df['security_deposit'] == 0]) / len(df) * 100) # 30% of listings don't charge security deposit
# lets find mean
print('Mean value of security deposit, $:')
entire_home['security_deposit'].mean(skipna=True)

# distribution of price for extra people
print('Hosts who dont charge anything for extra people')
print(len(df.loc[df['extra_people'] == 0]) / len(df) * 100) # 42% of listings don't charge anything for extra people

# see percentage of listings without reviews
print('Percentage of listings without reviews:')
print(len(df.loc[df['number_of_reviews'] == 0]) / len(df) * 100) # 12% of listings don't have reviews