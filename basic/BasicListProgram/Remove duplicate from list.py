
# coding: utf-8

# In[ ]:


# program to remove dublicate value from list without using build in function

lis=[1,2,3,2,2,4,1,5,3,2,3,4,4,2,2,2,1,18,7,54]
lis.sort()
print(lis)
k=1
newlis=[]
for i in range(0,len(lis)):
    j=i+k
    flag=0
    for j in range(j,len(lis)):
        #print(lis[i],lis[j])
        if lis[i]!=-1:
            if lis[i]==lis[j]:
                lis[j]=-1
                                
for i in lis:
    if i!=-1:
        newlis.append(i)
print(newlis)
                

