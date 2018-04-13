
# coding: utf-8

# In[2]:


import pandas as pd
sales = [{'account': 'Jones LLC', 'Jan': 150, 'Feb': 200, 'Mar': 140},
         {'account': 'Alpha Co',  'Jan': 200, 'Feb': 210, 'Mar': 215},
         {'account': 'Blue Inc',  'Jan': 50,  'Feb': 90,  'Mar': 95 }]
df = pd.DataFrame(sales)
df


# In[8]:


t=df['Feb'].max()
df[df['Feb']==t]


# In[61]:


revenue=[{'Date':'1/10/17','New York':87,'Los Angeless':222 },
         {'Date':'1/14/17','New York':' ','Los Angeless':13 },
         {'Date':'1/14/17','New York':8447,'Los Angeless':29},
         {'Date':'1/134/17','New York':78878,'Los Angeless': '  '},
         {'Date':'1/31/17','New York':855,'Los Angeless':882},
         {'Date':'1/13/17','New York':8445,'Los Angeless':452 },
         {'Date':'1/1/17','New York':8455,'Los Angeless':562 },
         {'Date':'1/12/17','New York':3434,'Los Angeless':562 },
         {'Date':'1/1/17','New York':344,'Los Angeless':542 }
        ] 
df1=pd.DataFrame(revenue)


# In[62]:


print(df1)


# In[63]:


type(df1)


# In[64]:


print(df1)


# In[75]:


df1.Date


# In[76]:


df1["Los Angeless"]


# In[98]:


#df1[["Los Angeless","Date"]]
df1.insert(3,column="sport",value="Basketball")


# In[100]:


df1


# In[106]:




