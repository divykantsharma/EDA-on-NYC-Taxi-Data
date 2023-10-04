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
for p in ax.patches:
    height = p.get_height()
    ax.text(x = p.get_x() + (p.get_width()/2),
    y = height+0.2, ha = 'center', s = '{:.0f}'.format(height)) 
    # takes height value, formats it as a string with no decimal places,and assigns the formatted string to the variable s
plt.show()


# ## Plot 2: Distribution of each day in a week - Number of daily pickups and drop offs

# In[20]:


figure, ax=plt.subplots(nrows=1,ncols=2,figsize=(10,5)) # setting the basic stri

sns.countplot(x='pickup_day',data=data,ax=ax[0])
ax[0].set_title(' no of pickups done on each day of the week')

sns.countplot(x='dropoff_day',data=data,ax =ax[1])
ax[1].set_title('no of dropoffs done on each day of the week')

plt.show()


# ## Plot 3: Trip Duration Distribution

# In[21]:


data.columns


# In[22]:


# trip_Duration distribution

x = data['trip_duration']
sns.distplot(x)
plt.show()


# ## Plot 4: Distribution of pickup timezone

# In[23]:


data.head()


# In[24]:


data.columns


# In[25]:


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


# In[26]:


ax = sns.countplot(x=data['pickup_timezone'])
plt.title('Distribution of pickup_timezone')  
for p in ax.patches:
    height = p.get_height()
    ax.text(x = p.get_x() + (p.get_width()/2),
    y = height+0.2, ha = 'center', s = '{:.0f}'.format(height))
plt.show()


# ## Plot 5: Distribution of active hours - pickup and drop off

# In[27]:


data.columns


# In[28]:


# Using an histogram
figure, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (10,5)) # setting the basic structure for visualization

data['pickup_hour'] = data['pickup_datetime'].dt.hour
data.pickup_hour.hist(bins = 24, ax = ax[0])
ax[0].set_title('Distribution of pickup hours')

data['dropoff_hour'] = data['dropoff_datetime'].dt.hour
data.dropoff_hour.hist(bins = 24, ax = ax[1])
ax[1].set_title('Distribution of dropoff hours')

plt.tight_layout() # to remove the line - Text(0.5, 1.0, 'Distribution of dropoff hours') from the visualization


# ## Plot 6: Distribution of pickup and dropoff months

# In[29]:


ax = sns.countplot(x = data['pickup_month'])
plt.title('Distribution of total pickup month')

for p in ax.patches:
    height = p.get_height()
    ax.text(x = p.get_x() + (p.get_width()/2),
    y = height+0.2, ha = 'center', s = '{:.0f}'.format(height))
plt.show()


# In[30]:


ax = sns.countplot(x = data['dropoff_month'])
plt.title(' Distribution of total dropoff month')

for p in ax.patches:
    height = p.get_height()
    ax.text(x = p.get_x() + (p.get_width()/2),
    y = height+0.2, ha = 'center', s = '{:.0f}'.format(height))
plt.show()


# ## Plot 7: Distribution of total pickup hour

# In[31]:


data.columns


# In[32]:


ax = sns.countplot(x = data['pickup_hour'])
plt.title(' Distribution of total pickup_hour')

for p in ax.patches:
    height = p.get_height()
    ax.text(x = p.get_x() + (p.get_width()/2),
    y = height+0.2, ha = 'center', s = '{:.0f}'.format(height))
plt.show()

