#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df = pd.read_excel("Downloads/gradedata.xlsx") 
df.head()
bins=[0,80,100]
group_names = ['Fail', 'Pass']
df['passfail'] = pd.cut(df['grade'], bins, labels = group_names)
df.head(10)


# In[3]:


import numpy as np
df['isBusy'] = np.where((df['exercise']>3) & (df['hours']>17),'busy',' ')
df.tail(10)


# In[ ]:




