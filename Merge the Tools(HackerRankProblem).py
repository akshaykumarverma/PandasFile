
# coding: utf-8

# In[63]:


print('hello')


# In[ ]:





# In[67]:


lis = ['ABBCA', 'CCDDC','BBBACA', 'AASSAA']
lisnew=[]
for strtest in lis:
    count = 0
    strnew = ''

    while len(strtest) >= 1:
        count = count + 1
        remove = strtest[0]
        strnew = strnew + remove
        strtest = strtest.replace(remove, '')
        #print(strtest)
    print(strnew)
    




# In[89]:


import sys
lis=[]
strold = 'A'
n = 3
t=n
start = 0
print(len(strold))
end = int(len(strold) / n)
for i in range(0, end):
    lis.append((strold[start:n]))
    start = n
    n = n + t
print(lis)
lisnew=[]
for strtest in lis:
    count = 0
    strnew = ''

    while len(strtest) >= 1:
        count = count + 1
        remove = strtest[0]
        strnew = strnew + remove
        strtest = strtest.replace(remove, '')
        #print(strtest)
    print(strnew)


