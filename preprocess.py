#!/usr/bin/env python
# coding: utf-8

# In[38]:


import zipfile
with zipfile.ZipFile("Data.zip", 'r') as zip_ref:
    zip_ref.extractall()


# In[39]:


get_ipython().system('tar -xvzf Data/Hugo.tar.gz -C Data/ && rm Data/Hugo.tar.gz')
get_ipython().system('tar -xvzf Data/Tolstoy.tar.gz -C Data/ && rm Data/Tolstoy.tar.gz')
get_ipython().system('tar -xvzf Data/shakespeare.tar.gz -C Data/ && rm Data/shakespeare.tar.gz')
get_ipython().system('mkdir Data/shakespeare')


# In[42]:


get_ipython().system("ls Data/ | grep -Ev 'Tolstoy|Hugo|shakespeare'|  xargs printf -- 'Data/%s\\n' | xargs mv -t Data/shakespeare")


# In[ ]:




