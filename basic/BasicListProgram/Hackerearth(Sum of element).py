
# coding: utf-8

# In[89]:


#program to find the sum of distinct element sum is present or not in lis


lis=[1,2,3,4,5,9,7]
k=1
sum=0
import sys
for i in range(0,len(lis)):
    j=i+k
    for j in range(j,len(lis)):
        sum=lis[i]+lis[j]
        if sum in lis:
            #print('sum is ' +%d ' i and j is ',sum,lis[i],lis[j])
            print("Total sum is ", sum, "pair", lis[i],lis[j])

        


# In[142]:




