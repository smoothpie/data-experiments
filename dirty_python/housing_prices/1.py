#%%
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('~/code/data/housing_prices/train.csv')
data.head()

# assumptions: overallqual neighborhood, housestyle, yearbuilt, grlivarea, BedroomAbvGr, Fireplaces, GarageArea influence price
data.corr()
# so yeah: OverallQual is 79% correlated with price
# GarageArea is 56% corr with OverallQual and GarageCars is 60%. GrLivArea is 59%. YearBuilt is 57%
# YearBuilt is 82% with GarageYrBlt which is logical and 52% with SalePrice
# GrLivArea is 70% with price
# GaraceCars is 64% with price and GarageArea is 62%
# So everything is as expected.

data.isnull().sum()

# before going further in analysing the data set, it's very much required to see how the target variable is behaving
# min = data['SalePrice'].min()
# print('Min Selling Price is:', min)
# max = data['SalePrice'].max()
# print('Max Selling Price is:', max)
# avg = data['SalePrice'].mean()
# print('Average Selling Price is:', avg)
# median = data['SalePrice'].median()
# print('Median Selling Price is:', median)

# data['SalePrice'].plot.hist(bins=30, edgecolor='black', color='green')
# fig=plt.gcf()
# fig.set_size_inches(25,15)
# x_range = range(0,750000,25000)
# plt.xticks(x_range)
# price seems to follow a slightly skewed pattern from the standard Normal Distribution curve

# it becomes hard to comment on single values of a variable which is continuous in nature and can be having
# too many values. So categorizing it comes to rescue
data['SalePrice_Cat'] = 0
data.loc[data.SalePrice <= 100000, 'SalePrice_Cat'] = 0
data.loc[(data.SalePrice > 100000) & (data.SalePrice <= 250000), 'SalePrice_Cat'] = 1
data.loc[data.SalePrice > 250000, 'SalePrice_Cat'] = 2

data['SalePrice_Cat'].value_counts()
# sns.countplot('SalePrice_Cat', data=data, color='blue')

# along with above categorization we can also look for quantile based segregation
# which buckets the data in buckets of equal number of houses
data['SalePrice_qcut_Cat'] = 0
data['SalePrice_qcut_Cat'] = pd.qcut(data['SalePrice'], 20)

data['SalePrice_qcut_Cat'].value_counts()

# fig, axes = plt.subplots(1,2,figsize=(18,5))
# sns.countplot('MSSubClass', data=data, ax=axes[0], color='blue')
# sns.countplot('MSSubClass', hue='SalePrice_Cat', data=data, ax=axes[1])

pd.crosstab([data.SalePrice_Cat],[data.MSSubClass],margins=True).style.background_gradient(cmap='summer_r')
# houses with MSSubClass >= 70 have higher chances of having medium selling price than within the range of 1| to 2|

pd.crosstab([data.SalePrice_qcut_Cat],[data.MSSubClass],margins=True).style.background_gradient('summer_r')
# Looks like nothing much is coming out from quantile based categorization(or binning).

# lets look on other variables
# print(data['GrLivArea'].isnull().sum())
# print(data['OverallQual'].isnull().sum())
# print(data['OverallCond'].isnull().sum())
# print(data['Neighborhood'].isnull().sum())

# print("OverallQual")
# print(data['OverallQual'].value_counts())
# and for each

# pd.crosstab([data.SalePrice_Cat],[data.OverallQual],margins=True).style.background_gradient('summer_r')

# fig, axes = plt.subplots(1,2,figsize=(18,5))
# sns.countplot('OverallQual',data=data,ax=axes[0])
# sns.countplot('OverallQual',hue='SalePrice_Cat',data=data,ax=axes[1])
# plt.show()

# pd.crosstab([data.SalePrice_Cat],[data.OverallCond],margins=True).style.background_gradient('summer_r')

# fig, axes = plt.subplots(1,2,figsize=(18,5))
# sns.countplot('OverallCond',data=data,ax=axes[0])
# sns.countplot('OverallCond',hue='SalePrice_Cat',data=data,ax=axes[1])
# plt.show()

# pd.crosstab([data.SalePrice_Cat],[data.Neighborhood],margins=True).style.background_gradient('summer_r')

# fig, axes = plt.subplots(1,2,figsize=(18,5))
# sns.countplot('Neighborhood',data=data,ax=axes[0])
# sns.countplot('Neighborhood',hue='SalePrice_Cat',data=data,ax=axes[1])
# plt.show()

# min_grliv_area = data['GrLivArea'].min()
# print("Min GrLiveArea is :", min_grliv_area)
# avg_grliv_area = data['GrLivArea'].mean()
# print("Average GrLiveArea is :", avg_grliv_area)
# median_grliv_area = data['GrLivArea'].median()
# print("Median GrLiveArea is :", median_grliv_area)
# max_grliv_area = data['GrLivArea'].max()
# print("Max GrLiveArea is :", max_grliv_area)

# data['GrLivArea'].plot.hist(bins=20,edgecolor='black',color='yellow')
# plt.xticks(range(0,5642,275))

# data['GrLivArea_Cat'] = 0
# data['GrLivArea_Cat'] = pd.qcut(data['GrLivArea'],10)

# data['GrLivArea_Cat'].value_counts()

# pd.crosstab([data.GrLivArea_Cat],[data.SalePrice_Cat],margins=True).style.background_gradient('summer_r')
# its visible that as the living area increases, number of houses in higher pricing category increases

# print(data['YearRemodAdd'].min())
# print(data['YearRemodAdd'].max())

data['RemodelYear_Cat'] = 0
data.loc[data.YearRemodAdd <= 1950, 'RemodelYear_Cat'] = 0
data.loc[(data.YearRemodAdd > 1950) & (data.YearRemodAdd <= 1960), 'RemodelYear_Cat'] = 1
data.loc[(data.YearRemodAdd > 1960) & (data.YearRemodAdd <= 1970), 'RemodelYear_Cat'] = 2
data.loc[(data.YearRemodAdd > 1970) & (data.YearRemodAdd <= 1980), 'RemodelYear_Cat'] = 3
data.loc[(data.YearRemodAdd > 1980) & (data.YearRemodAdd <= 1990), 'RemodelYear_Cat'] = 4
data.loc[(data.YearRemodAdd > 1990) & (data.YearRemodAdd <= 2000), 'RemodelYear_Cat'] = 5
data.loc[(data.YearRemodAdd > 2000) & (data.YearRemodAdd <= 2010), 'RemodelYear_Cat'] = 6

data['RemodelYear_Cat'].value_counts()

# fig, axes = plt.subplots(1,2,figsize=(18,5))
# sns.countplot('RemodelYear_Cat',data=data,ax=axes[0])
# sns.countplot('RemodelYear_Cat',hue='SalePrice_Cat',data=data,ax=axes[1])
# its seen that only houses that have been remodelled have got higher prices bar

data['RoofStyle'].value_counts()
# data['RoofStyle'].value_counts().plot.pie()

# fig, axes = plt.subplots(1,2,figsize=(18,5))
# sns.countplot('RoofStyle',data=data,ax=axes[0])
# sns.countplot('RoofStyle',hue='SalePrice_Cat',data=data,ax=axes[1])
# nothing too interesting

data['SaleCondition'].value_counts()
# fig, axes = plt.subplots(1,2,figsize=(18,5))
# sns.countplot('SaleCondition',data=data,ax=axes[0])
# sns.countplot('SaleCondition',hue='SalePrice_Cat',data=data,ax=axes[1])

data['YrSold'].value_counts()
# fig, axes = plt.subplots(1,2,figsize=(18,5))
# sns.countplot('YrSold',data=data,ax=axes[0])
# sns.countplot('YrSold',hue='SalePrice_Cat',data=data,ax=axes[1])

data['LotShape'].value_counts()
# fig, axes = plt.subplots(1,2,figsize=(18,5))
# sns.countplot('LotShape',data=data,ax=axes[0])
# sns.countplot('LotShape',hue='SalePrice_Cat',data=data,ax=axes[1])

# print(data['YearBuilt'].min())
# print(data['YearBuilt'].max())
data['YearBuilt_Cat'] = 0
data.loc[data.YearBuilt <= 1880,'YearBuilt_Cat'] = 0
data.loc[(data.YearBuilt > 1880) & (data.YearBuilt <= 1890),'YearBuilt_Cat'] = 1
data.loc[(data.YearBuilt > 1890) & (data.YearBuilt <= 2000),'YearBuilt_Cat'] = 2
data.loc[(data.YearBuilt > 2000) & (data.YearBuilt <= 2010),'YearBuilt_Cat'] = 3
data.loc[data.YearBuilt > 2010,'YearBuilt_Cat'] = 4

fig, axes = plt.subplots(1,2,figsize=(18,5))
sns.countplot('YearBuilt_Cat',data=data,ax=axes[0],color='blue')
sns.countplot('YearBuilt_Cat',hue='SalePrice_Cat',data=data,ax=axes[1])
# nothing much informative so far as well

# so some of the variables that has got some info/insight are:
# MSSubClass, OverallQuality, Living Area above ground, year of remodelling and neighborhood