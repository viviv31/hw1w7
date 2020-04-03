#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np

all_data = pd.DataFrame()

for i in range(0,103):
    file = "Downloads/weekdata_" + str(i).zfill(3) + ".xlsx"
    all_data = all_data.append(pd.read_excel(file),ignore_index=True)

all_data.describe()


# In[ ]:





# In[ ]:




