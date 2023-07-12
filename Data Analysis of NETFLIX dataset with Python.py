#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
df=pd.read_csv(r'Netflix_Dataset.csv')
df
df.head()
df.tail()
df.shape
df.size
df.columns
df.dtypes
df.info()
df[df.duplicated()]
df.drop_duplicates()
df.drop_duplicates(inplace= True)
df[df.duplicated()]
df.shape
df.isnull()
df.isnull().sum()
#seaborn library
import seaborn as sns
sns.heatmap(df.isnull())
#Q. 1) For 'Friends', what is the Show Id and Who is the Director of this show ?
df[df['Title'].isin(['Friends'])]
df[df['Title'].str.contains('Friends')]
#Q. 2) In which year the highest number of the TV Shows & Movies were released ? Show with Bar Graph.
df.dtypes
df['Date_N']=pd.to_datetime(df['Release_Date'])
df
df.dtypes
df['Date_N'].dt.year.value_counts()
df['Date_N'].dt.year.value_counts().plot(kind='bar')
#Q. 3) How many Movies & TV Shows are in the dataset ? Show with Bar Graph.
df.groupby('Category').Category.count()
sns.countplot(df['Category'])
#Q. 4) Show all the Movies that were released in year 2000.
#Creating new column
df.head(2)
df['Year']=df['Date_N'].dt.year
df.head(2)
df[(df['Category']== 'Movie')&(df['Year']==2000)]
df[(df['Category']== 'Movie')&(df['Year']==2020)]
#Q. 5) Show only the Titles of all TV Shows that were released in India only.
df[ (df['Category']=='TV Show') & (df['Country']=='India')]['Title']
#Q. 6) Show Top 10 Directors, who gave the highest number of TV Shows & Movies to Netflix ?
df['Director'].value_counts().head(10)
#Q. 7) Show all the Records, where "Category is Movie and Type is Comedies" or "Country is India".
df[(df['Category']=='Movie')&(df['Type']=='Comedies')]
df[(df['Category']=='Movie')&(df['Type']=='Comedies') | (df['Country']=='India')]
#Q. 8) In how many movies/shows, Tom Cruise was cast ?
df[df['Cast']=='Tom Cruise']
df[df['Cast'].str.contains('Tom Cruise')]
#Creating new data-frame
data_new= df.dropna()
data_new.head(2)
data_new[data_new['Cast'].str.contains('Tom Cruise')]
#Q. 9) What are the different Ratings defined by Netflix ?
df['Rating'].unique()
#Q. 9.1) How many Movies got the 'TV-14' rating, in Canada ?
df[(df['Category']=='Movie')&(df['Rating']=='TV-14')].shape
df[(df['Category']=='Movie')&(df['Rating']=='TV-14')&(df['Country']=='Canada')]
#Q. 9.2) How many TV Shows got the 'R' rating, after year 2018 ?
df[(df['Category']=='TV Show')&(df['Rating']=='R')&(df['Year']>2018)]
#Q. 10) What is the maximum duration of a Movie/Show on Netflix ?
df.Duration.unique()
df.Duration.dtypes
#str.split()
df[['Minutes','Unit']]=df['Duration'].str.split(' ',expand=True)
df.head(2)
df['Minutes'].max()
df['Minutes'].mean()
df.dtypes
#Q. 11) Which individual country has the Highest No. of TV Shows ?
data_tvshow=df[df['Category']=='TV Show']
data_tvshow.head(2)
data_tvshow.Country.value_counts()
data_tvshow.Country.value_counts().head(1)
#Q. 12) How can we sort the dataset by Year ?
df.sort_values(by='Year')
df.sort_values(by='Year',ascending=False).head(10)
#Q. 13) Find all the instances where: Category is 'Movie' and Type is 'Dramas' or Category is 'TV Show' & Type is 'Kids' TV'.
df[(df['Category']=='Movie')&(df['Type']=='Dramas')].head(2)
df[(df['Category']=='TV Show')&(df['Type']=="Kids' TV")]
df[(df['Category']=='Movie')&(df['Type']=='Dramas')|(df['Category']=='TV Show')&(df['Type']=="Kids' TV")]


# In[ ]:




