
# coding: utf-8

# In[16]:


print('hello')


# In[2]:


import pandas as pd
import numpy as np
import matplotlib .pyplot as plt
from matplotlib import style
get_ipython().run_line_magic('pinfo', 'pd.Series')
style.use('ggplot')


# In[3]:


web_stats={'Day':[1,2,3,4,5],
          'Visitors' :[43,53,45,76,55],
          'Bounce_Rate':[65,72,73,559,9]}
df=pd.DataFrame(web_stats)
    


# In[4]:


print(df)


# In[25]:


df['Bounce_Rate'].max()


# In[6]:


print(df['Day'])


# In[7]:


print(df.Day.tolist())


# In[8]:


print('hello')


# In[9]:


animal=['tiger','dog','cat']
print(animal)


# In[10]:


pd .Series(animal)


# In[11]:


s=pd.Series(np.random.randint(0,1000,10000))
s.head


# In[12]:


len(s)


# In[13]:


get_ipython().run_cell_magic('timeit', '-n 100 ', 'summary =0\nfor item in s:\n    summary+=item\n    ')


# In[14]:


s=pd.Series([100,10000,10001,1101,12])


# In[15]:


s=s+2
print(s
     )


# In[16]:


s=pd.Series([1,2,3,4])
s.loc['animal']='Bears'


# In[17]:


print(s
     )


# In[18]:


purchase1=pd.Series({'Name':'Akshay',
                   'Item':'Purchased',
                   'cost':223})
purchase2=pd.Series({'Name':'Hero',
                   'Item':'Purchased',
                   'cost':223})
purchase3=pd.Series({'Name':'kumar',
                   'Item':'Purchased',
                   'cost':3223})
df=pd.DataFrame([purchase1,purchase2,purchase3],index=['store1','store2','store3'])


# In[19]:


df.head()


# In[20]:


df.loc['store2']


# In[60]:


type(df.loc['store2'])


# In[63]:


df.loc['store1','Item']


# In[66]:


df.loc['store3']


# In[67]:


df.T


# In[71]:


df.T.loc['cost']


# In[74]:


df.T.loc['Name']['store3']


# In[75]:


pwd


# In[88]:


df=pd.read_csv('/users/akshaykumar/desktop/PERTH-LONMETALS (1).csv',index_col=0,skiprows=0)


# In[89]:


print(df.head())


# In[90]:


df.columns


# In[ ]:


for col in  df.columns:
    if col[0:2]== '01':
        df.rename(columns={})

