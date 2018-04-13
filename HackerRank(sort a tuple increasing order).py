
# coding: utf-8

# In[107]:


# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
list1=[(1, 7), (1, 3), (3, 4, 5), (2, 2)]
#list1=[(1, 3), (3, 2), (2, 1)]
#list1=[(2, 3), (1, 2), (3, 1)]
list2=[]
list3=[]
def sort_last(tuples):
    for i in tuples:
        t=list(i)
        t.sort()
        k=tuple(t)
        list2.append((k))
        
    #print(list2)
    newlis=[]
    for i in list2:
        #print(i[-1])
        t=i[-1]
        #print(t)
        newlis.append(t)
        #print(newlis)
        newlis.sort()
        #print(newlis)
     
    for i in newlis:
        #print(i)
        for j in list1:
            #print(j)
            if i==j[-1]:
                list3.append(j)
    return list3
                
    
sort_last(list1)

