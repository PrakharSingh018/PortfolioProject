#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
df=pd.read_csv(r'Netflix_Dataset.csv')
df


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.shape


# In[7]:


df.size


# In[8]:


df.columns


# In[9]:


df.dtypes


# In[11]:


df.info()


# In[ ]:


#Task. 1) Is there any Duplicate Record in this dataset ? If yes, then remove the duplicate records.


# In[14]:


df[df.duplicated()]


# In[15]:


df.drop_duplicates()


# In[16]:


df.drop_duplicates(inplace= True)


# In[17]:


df[df.duplicated()]


# In[18]:


df.shape


# In[ ]:


#Task. 2) Is there any Null Value present in any column ? Show with Heat-map.


# In[19]:


df.isnull()


# In[20]:


df.isnull().sum()


# In[ ]:


#seaborn library


# In[22]:


import seaborn as sns


# In[23]:


sns.heatmap(df.isnull())


# In[ ]:


Q. 1) For 'Friends', what is the Show Id and Who is the Director of this show ?


# In[24]:


df.head()


# In[26]:


df[df['Title'].isin(['Friends'])]


# In[27]:


df[df['Title'].str.contains('Friends')]


# In[ ]:


#Q. 2) In which year the highest number of the TV Shows & Movies were released ? Show with Bar Graph.


# In[29]:


df.dtypes


# In[47]:


df['Date_N']=pd.to_datetime(df['Release_Date'])


# In[48]:


df


# In[49]:


df.dtypes


# In[50]:


df['Date_N'].dt.year.value_counts()


# In[51]:


df['Date_N'].dt.year.value_counts().plot(kind='bar')


# In[ ]:


#Q. 3) How many Movies & TV Shows are in the dataset ? Show with Bar Graph.


# In[53]:


df.groupby('Category').Category.count()


# In[54]:


sns.countplot(df['Category'])


# In[ ]:


#Q. 4) Show all the Movies that were released in year 2000.


# In[57]:


#Creating new column
df.head(2)


# In[55]:


df['Year']=df['Date_N'].dt.year


# In[58]:


df.head(2)


# In[65]:


df[(df['Category']== 'Movie')&(df['Year']==2000)]


# In[66]:


df[(df['Category']== 'Movie')&(df['Year']==2020)]


# In[ ]:


#Q. 5) Show only the Titles of all TV Shows that were released in India only.


# In[75]:


df


# In[77]:


df[ (df['Category']=='TV Show') & (df['Country']=='India')]['Title']


# In[ ]:


#Q. 6) Show Top 10 Directors, who gave the highest number of TV Shows & Movies to Netflix ?


# In[78]:


df.head(2)


# In[80]:


df['Director'].value_counts().head(10)


# In[ ]:


#Q. 7) Show all the Records, where "Category is Movie and Type is Comedies" or "Country is India".


# In[81]:


df[(df['Category']=='Movie')&(df['Type']=='Comedies')]


# In[83]:


df[(df['Category']=='Movie')&(df['Type']=='Comedies') | (df['Country']=='India')]


# In[ ]:


#Q. 8) In how many movies/shows, Tom Cruise was cast ?


# In[84]:


df[df['Cast']=='Tom Cruise']


# In[86]:


df[df['Cast'].str.contains('Tom Cruise')]


# In[ ]:


#Creating new data-frame


# In[88]:


data_new= df.dropna()


# In[89]:


data_new.head(2)


# In[90]:


data_new[data_new['Cast'].str.contains('Tom Cruise')]


# In[ ]:


#Q. 9) What are the different Ratings defined by Netflix ?


# In[91]:


df.head(2)


# In[92]:


df['Rating'].unique()


# In[ ]:


#Q. 9.1) How many Movies got the 'TV-14' rating, in Canada ?


# In[93]:


df.head(2)


# In[97]:


df[(df['Category']=='Movie')&(df['Rating']=='TV-14')].shape


# In[99]:


df[(df['Category']=='Movie')&(df['Rating']=='TV-14')&(df['Country']=='Canada')]


# In[ ]:


#Q. 9.2) How many TV Shows got the 'R' rating, after year 2018 ?


# In[102]:


df[(df['Category']=='TV Show')&(df['Rating']=='R')&(df['Year']>2018)]


# In[ ]:


#Q. 10) What is the maximum duration of a Movie/Show on Netflix ?


# In[103]:


df.head(2)


# In[104]:


df.Duration.unique()


# In[105]:


df.Duration.dtypes


# In[ ]:


#str.split()


# In[106]:


df.head()


# In[108]:


df[['Minutes','Unit']]=df['Duration'].str.split(' ',expand=True)


# In[109]:


df.head(2)


# In[111]:


df['Minutes'].max()


# In[112]:


df['Minutes'].mean()


# In[114]:


df.dtypes


# In[ ]:


#Q. 11) Which individual country has the Highest No. of TV Shows ?


# In[115]:


df.head(2)


# In[117]:


data_tvshow=df[df['Category']=='TV Show']


# In[118]:


data_tvshow.head(2)


# In[119]:


data_tvshow.Country.value_counts()


# In[120]:


data_tvshow.Country.value_counts().head(1)


# In[ ]:


#Q. 12) How can we sort the dataset by Year ?


# In[121]:


df.head(2)


# In[122]:


df.sort_values(by='Year')


# In[123]:


df.sort_values(by='Year',ascending=False).head(10)


# In[ ]:


#Q. 13) Find all the instances where: Category is 'Movie' and Type is 'Dramas' or Category is 'TV Show' & Type is 'Kids' TV'.


# In[124]:


df.head(2)


# In[125]:


df[(df['Category']=='Movie')&(df['Type']=='Dramas')].head(2)


# In[128]:


df[(df['Category']=='TV Show')&(df['Type']=="Kids' TV")]


# In[130]:


df[(df['Category']=='Movie')&(df['Type']=='Dramas')|(df['Category']=='TV Show')&(df['Type']=="Kids' TV")]


# In[ ]:




