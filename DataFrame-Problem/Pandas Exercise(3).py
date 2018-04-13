
# coding: utf-8

# In[3]:


import pandas as pd 

user= pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', 
                      sep='|', index_col='user_id')
user.head()


# In[5]:


user.head(25)


# In[15]:


user.tail(10)


# In[22]:


user.shape[0]


# In[23]:


user.shape[1]


# In[30]:


user.columns


# In[31]:


user.dtypes


# In[41]:


user['occupation']


# In[74]:


test=user.groupby('occupation').count()
test=user.occupation.value_counts()


# In[84]:


user.describe(include='all')


# In[86]:


user.age.mean()


# In[92]:


user.age.value_counts()


# In[93]:


t=pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv')


# In[94]:


t.head()


# In[153]:


t.sort_values('item_name')
test=t.drop_duplicates(['item_name','quantity'])


# In[154]:


t1=t.sort_values(by='item_price', ascending = False)
type(t1)


# In[156]:


t1.index


# In[158]:


t1.loc['2624']

