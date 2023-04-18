#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv(r"C:\Users\charl\Downloads\INFO 450\workout_data.csv")


# In[3]:


import plotly.express as px


# In[4]:


df


# In[5]:


get_ipython().system(' pip install plotly')


# In[11]:


fig = px.bar(df, x="Duration", y="Calories")
fig.show()


# In[13]:


fig = px.scatter_matrix(df, dimensions=["Duration", "Pulse", "Maxpulse", "Calories"])
fig.show()


# In[15]:


fig = px.box(df, x="Duration", y="Calories")
fig.show()


# In[ ]:




