
# coding: utf-8

# In[16]:


print('hello')


# In[38]:


import pandas as pd
import numpy as np
import matplotlib .pyplot as plt
from matplotlib import style
get_ipython().run_line_magic('pinfo', 'pd.Series')
style.use('ggplot')


# In[39]:


web_stats={'Day':[1,2,3,4,5],
          'Visitors' :[43,53,45,76,55],
          'Bounce_Rate':[65,72,73,559,9]}
df=pd.DataFrame(web_stats)
    


# In[40]:


print(df)


# In[21]:


print(df.tail(3))


# In[28]:


print(df['Day'])


# In[29]:


print(df.Day.tolist())


# In[30]:


print('hello')


# In[31]:


animal=['tiger','dog','cat']
print(animal)


# In[32]:


pd .Series(animal)


# In[42]:


s=pd.Series(np.random.randint(0,1000,10000))
s.head


# In[43]:


len(s)


# In[45]:


get_ipython().run_cell_magic('timeit', '-n 100 ', 'summary =0\nfor item in s:\n    summary+=item\n    ')


# In[46]:


s=pd.Series([100,10000,10001,1101,12])


# In[47]:


s=s+2
print(s
     )


# In[48]:


s=pd.Series([1,2,3,4])
s.loc['animal']='Bears'


# In[49]:


print(s
     )


# In[57]:


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


# In[58]:


df.head()


# In[59]:


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

