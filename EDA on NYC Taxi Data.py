#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis on NYC Taxi Data

# ## Exploring and Examining the Data

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from datetime import datetime
import datetime


# In[2]:


data=pd.read_csv('train.csv')


# In[3]:


data.shape


# In[4]:


data.columns


# In[5]:


data.head()


# In[6]:


data.dtypes


# In[7]:


data['pickup_datetime']=pd.to_datetime(data['pickup_datetime'])
data['dropoff_datetime']=pd.to_datetime(data['dropoff_datetime'])


# In[8]:


data.dtypes


# In[9]:


data['pickup_day']=data['pickup_datetime'].dt.day_name()
data['dropoff_day']=data['dropoff_datetime'].dt.day_name()


# In[10]:


data.head()


# In[11]:


data['pickup_month']=pd.DatetimeIndex(data['pickup_datetime']).month
data['dropoff_month']=pd.DatetimeIndex(data['dropoff_datetime']).month


# In[12]:


data.head()


# In[13]:


data.dtypes


# In[14]:


data.shape


# In[15]:


data['pickup_day'].value_counts()


# In[16]:


data.head()


# In[17]:


data['dropoff_day'].value_counts()


# In[18]:


data.describe()


# # Further Analysis

# ## Plot 1: Distribution of Passenger Count - Number of Passengers in each taxi

# In[19]:


ax=sns.countplot(x=data['passenger_count'])
plt.title('Distribution of Passeger Count')


# In[20]:


# Labelling the plot with the values
ax=sns.countplot(x = data['passenger_count'])
plt.title(' Distribution of Passenger Count')

for p in ax.patches:
    height = p.get_height()
    ax.text(x = p.get_x() + (p.get_width()/2),
    y = height+0.2, ha = 'center', s = '{:.0f}'.format(height))
plt.show()


# ## Plot 2: Distribution of each day in a week - Number of daily pickups and drop offs

# In[21]:


figure, ax=plt.subplots(nrows=1,ncols=2,figsize=(10,5))
sns.countplot(x='pickup_day',data=data,ax=ax[0])
ax[0].set_title(' no of pickups done on each day of the week')

sns.countplot(x='dropoff_day',data=data,ax =ax[1])
ax[1].set_title('no of dropoffs done on each day of the week')

# plt.tight_layout()


# ## Plot 3: Trip Duration Distribution

# In[22]:


data.columns


# In[23]:


# trip_Duration distribution

x = data['trip_duration']
sns.distplot(x)


# ## Plot 4: Distribution of pickup timezone

# In[24]:


data.head()


# In[25]:


data.columns


# In[26]:


def timezone(x):
    if x>=datetime.time(4, 0, 1) and x <=datetime.time(10, 0, 0):
        return 'morning'
    elif x>=datetime.time(10, 0, 1) and x <=datetime.time(16, 0, 0):
        return 'midday'
    elif x>=datetime.time(16, 0, 1) and x <=datetime.time(22, 0, 0):
        return 'evening'
    elif x>=datetime.time(22, 0, 1) or x <=datetime.time(4, 0, 0):
        return 'late night'
    
data['pickup_timezone']=data['pickup_datetime'].apply(lambda x :timezone(datetime.datetime.strptime(str(x), "%Y-%m-%d %H:%M:%S").time()) )
data['dropoff_timezone']=data['dropoff_datetime'].apply(lambda x :timezone(datetime.datetime.strptime(str(x), "%Y-%m-%d %H:%M:%S").time()) )


# In[27]:


ax = sns.countplot(x=data['pickup_timezone']);
plt.title('Distribution of pickup_timezone')
for p in ax.patches:
    height = p.get_height()
    ax.text(x = p.get_x()+(p.get_width()/2), # x-coordinate position of data label, padded to be in the middle of the bar
    y = height+0.2, ha = 'center',s = '{:.0f}'.format(height)) # data label, formatted to ignore decimals
    #ha = ‘center’) # sets horizontal alignment (ha) to center
plt.xticks(rotation = 'vertical')    
plt.show()


# ## Plot 5: Distribution of active hours - pickup and drop off

# In[28]:


data.columns


# In[29]:


# Using an histogram
figure, ax = plt.subplots(nrows = 1, ncols=2, figsize = (10,5))

data['pickup_hour'] = data['pickup_datetime'].dt.hour
data.pickup_hour.hist(bins = 24, ax = ax[0])
ax[0].set_title('Distribution of pickup hours')

data['dropoff_hour'] = data['dropoff_datetime'].dt.hour
data.dropoff_hour.hist(bins = 24, ax = ax[1])
ax[1].set_title('Distribution of dropoff hours')

plt.tight_layout()


# ## Plot 6: Distribution of pickup and dropoff months

# In[30]:


ax = sns.countplot(x = data['pickup_month'])
plt.title('Distribution of total pickup month')

for p in ax.patches:
    height = p.get_height()
    ax.text(x = p.get_x() + (p.get_width()/2),
    y = height+0.2, ha = 'center', s = '{:.0f}'.format(height))
plt.show()


# In[31]:


ax = sns.countplot(x = data['dropoff_month'])
plt.title(' Distribution of total dropoff month')

for p in ax.patches:
    height = p.get_height()
    ax.text(x = p.get_x() + (p.get_width()/2),
    y = height+0.2, ha = 'center', s = '{:.0f}'.format(height))
plt.show()


# ## Plot 7: Distribution of total pickup hour

# In[32]:


data.columns


# In[33]:


ax = sns.countplot(x = data['pickup_hour'])
plt.title(' Distribution of total pickup_hour')

for p in ax.patches:
    height = p.get_height()
    ax.text(x = p.get_x() + (p.get_width()/2),
    y = height+0.2, ha = 'center', s = '{:.0f}'.format(height))
plt.show()

