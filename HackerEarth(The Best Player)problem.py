
# coding: utf-8

# In[104]:


lis=['3 2\n', 'surbhi 3\n', 'surpanakha 3\n', 'shreya 84','shreya 84','shreya 83']
lis = list(map(lambda s: s.strip(), lis))
print(lis)


# In[105]:


lis.sort()
print(lis)
dic={}
for i in range(1,len(lis)):
    #print(lis[i])
    splitnew= lis[i].split()
    print(splitnew[1])
    dic[int(splitnew[1])]=splitnew[0]
print('===dic=',dic)
newlist=[]
for i in dic.keys():
    newlist.append(int(i))
newlist.sort(reverse=True)
print(newlist)
print(dic[3])



for i in range(0,2):
    j=i
    if j < len(newlist):
        if newlist[i] ==newlist[j]:
            print('same')
            
        


# In[100]:


dic={}
dicnew={}
for i in range(1,len(lis)):
    str=lis[i].split( )
    dic[str[0]]=int(str[1])
print(dic)

for key,value in dic.items():
    #print(value,key)
    dicnew[value]=key
print(dicnew)

