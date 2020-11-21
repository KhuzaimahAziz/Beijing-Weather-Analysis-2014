#!/usr/bin/env python
# coding: utf-8

# # Importing Important Libraries

# In[23]:


from  pandas import *
get_ipython().run_line_magic('matplotlib', 'inline')
from datetime import datetime


# # Reading CSV file

# In[12]:


China=pandas.read_csv('Beijing_PEK_2014.csv')
pandas.set_option('display.max_rows', None)
China


# In[13]:


China.columns 
#As You can see there are unnecessary spaces between different column names.In order to solve it we will use skipinitialspace command


# # Data Cleaning

# In[14]:


China=pandas.read_csv('Beijing_PEK_2014.csv', skipinitialspace=True)
China.columns 
#Now You can see that all the columns names are in sequence


# In[15]:


China 
#If you See the WindDirDegrees column this column have <br /> (HTML SYNtax) which will be problematic for us later in the program.


# In[16]:


China = China.rename(columns={'WindDirDegrees<br />': 'WindDirDegrees'}) 
China
#So we will use .rename command to rename the WindDirDegree Column.


# In[17]:


China['WindDirDegrees']=China['WindDirDegrees'].str.rstrip('<br />')
China
#Now all the values in the WindDirDegree have <br /> syntax. So we will have to strip this syntax from the values


# In[19]:


China['Events']=China['Events'].dropna()
China


# In[20]:


China.dtypes
#As you can see the WindDirDegrees column is in object data type also string data type. So we have to convert the data type of WindDirDegrees


# In[21]:


China['WindDirDegrees']=China['WindDirDegrees'].astype('int64')
China.dtypes
#Now you can see the data type of WindDirDegrees is changed to int64.


# In[25]:


China['Date']=to_datetime(China['Date'])
China.dtypes
#We also changed the data type of Date column to datetime


# # Visualizing the Date

# In[26]:


get_ipython().run_line_magic('matplotlib', 'inline')
China['Max Wind SpeedKm/h'].plot(grid=True, figsize=(10,5))
#But you can see on the x-axis name of months are not showing. So we will solve it by using .index.


# In[27]:


China.index=China['Date']
China[['Max Wind SpeedKm/h','Mean Wind SpeedKm/h']].plot(grid=True, figsize=(10,5))


# In[31]:


China[['Min TemperatureC','Mean TemperatureC', 'Max TemperatureC']].plot(grid=True, figsize=(20,5))


# In[29]:


China['Max Wind SpeedKm/h'].plot(grid=True, figsize=(10,5))


# # Report

# The best 2 weeks  in Beijing according to the analysis are 1st week of March and the last week of November Because as the graph shows in the month of March the Temperature is quite moderate and the Speed of Winds are also average 25km/h. Where as in the month November the Temperature is not very low and also the wind are on the average of 20km/h.

# In[ ]:




