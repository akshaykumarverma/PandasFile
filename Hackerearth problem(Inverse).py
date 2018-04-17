
# coding: utf-8

# In[71]:


'''There are many ways to order a list of integers from 1 to n. For example, if , the list could be : .
But there is a special way to create another list from the given list of integers. In this list, position of integer i is the  number in the given list. So following this rule, the given list will be written as: . This list is called inverse list. Now there exists some list whose inverse list is identical. For example, inverse list of  is same as given list. Given a list of integers you have to determine whether the list is inverse or not.
The input contains several test cases. The first line is the number of test cases t  . The first line of each test case contains an integer . Then a list of the integers 1 to n follows in the next line.

SAMPLE INPUT 
2
3
3 1 2
3
1 2 3
SAMPLE OUTPUT 
not inverse
inverse
'''


# In[122]:


li=['2', '3', '1243', '356', '7866', '3421', '653','3','234555','555432','1243']
new=''
for i in range(len(li)):
    new=new+li[i][::-1]
    strIndex = i+1
    if strIndex != len(li):
        if new in li[strIndex:-1]:
            print('inverse',new)
        else:
            print('not inverse')
    new=''
            
            
    

