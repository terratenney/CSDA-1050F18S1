#!/usr/bin/env python
# coding: utf-8

# In[120]:


import pandas as pd
import numpy as np


# In[121]:


data_schema = pd.read_csv("podcast18.csv")


# In[122]:


data = pd.read_fwf('Dictionary AI058 CdnPodcast 2018 FINALJun16 CLIENT.txt', header = 2)


# In[123]:


mapping = {}
data_schema_unique = df2.groupby(['Variable', 'Label']).size().reset_index(name='Freq')
for index, row in data_schema_unique.iterrows():
    if row['Label']:
        mapping[row['Variable']] = row['Label']


# In[124]:


data.rename(columns=mapping,inplace=True)


# In[125]:


data


# In[ ]:




