
# coding: utf-8

# In[1]:


# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
#def remove_adjacent(nums):

  #return
    
#print('remove_adjacent')
#  test(remove_adjacent()[1, 2, 2, 3]), [1, 2, 3]
 # test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  #test(remove_adjacent([]), [])
#[2,2,3,3,3]


# In[2]:


def remove_adjacent():
    test=[2,2,3,3,3]
    #test=[1,2,2,3]
    testnew=[]
    for i in test:
        if i not in testnew:
            testnew.append(i)
    testnew.sort()        
    #print(testnew)
    return testnew
remove_adjacent()    
    


# In[3]:


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
#def linear_merge(list1, list2):
  # +++your code here+++
  #return

# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.

#test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
 #      ['aa', 'bb', 'cc', 'xx', 'zz'])
  #test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
   #    ['aa', 'bb', 'cc', 'xx', 'zz'])
  #test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
  #     ['aa', 'aa', 'aa', 'bb', 'bb'])


# In[4]:


# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'
#def donuts(count):
 # return
    
    
    '''Number of donuts:  4
  X  got: None expected: 'Number of donuts: 4'
Number of donuts:  9
  X  got: None expected: 'Number of donuts: 9'
Number of donuts: many
  X  got: None expected: 'Number of donuts: many'
Number of donuts: many
  X  got: None expected: 'Number of donuts: many'
both_ends
  X  got: None expected: 'spng'
  X  got: None expected: 'Helo'
  X  got: None expected: ''
  X  got: None expected: 'xyyz'
fix_start
  X  got: None expected: 'ba**le'
  X  got: None expected: 'a*rdv*rk'
  X  got: None expected: 'goo*le'
  X  got: None expected: 'donut'
mix_up
  X  got: None expected: 'pox mid'
  X  got: None expected: 'dig donner'
  X  got: None expected: 'spash gnort'
  X  got: None expected: 'fizzy perm'''


# In[5]:



def donuts(count):
    if count > 9:
        return print('\'Number of donuts: many\'')
    else:
        return print('\'Number of donuts: '+str(count)+'\'')
donuts(61)    


# In[6]:


# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
#def both_ends(s):
 # for 
  #return
#both_ends('spring'), 'spng')
 # test(both_ends('Hello'), 'Helo')


# In[7]:


s='spring'
def both_ends(s):
    return print(s[0:2]+s[-2:])
    #print(s[-2:])
    
both_ends(s)    


# In[8]:



# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.
#def fix_start(s):
# +++your code here+++
#return
#print ('fix_start')
#test(fix_start('babble'), 'ba**le')
# test(fix_start('aardvark'), 'a*rdv*rk')
#test(fix_start('google'), 'goo*le')
#test(fix_start('donut'), 'donut')


# In[9]:


def fix_sarts():
    s='donut'
    s1=''
    s1=s1+s[0]
    for i in range(1,len(s)):
        if s[0]==s[i]:
            s1=s1+'*'
            #print(s1)
        else:
            s1=s1+s[i]
    return(s1)
        
fix_sarts() 
    


# In[10]:


# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
#def mix_up(a, b):
  
 # return
#print ('mix_up')
 # test(mix_up('mix', 'pod'), 'pox mid')
  #test(mix_up('dog', 'dinner'), 'dig donner')
  #test(mix_up('gnash', 'sport'), 'spash gnort')
  #test(mix_up('pezzy', 'firm'), 'fizzy perm')


# In[11]:


a='dog'
b='dinner'
def mix_up(a,b):
    t=''
    k=''
    k1=''
    k=k+b[0]
    k1=k1+a[0]
    for i in range(1,len(a)):
        k=k+a[i]
    for i in range(1,len(b)):
        k1=k1+b[i]
        
    return  k + ' ' + k1
mix_up(a,b)    
    
    


# In[12]:


# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.

# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
#def verbing(s):
  # +++your code here+++
  #return
 #print ('verbing')
  #test(verbing('hail'), 'hailing')
  #test(verbing('swiming'), 'swimingly')
  #test(verbing('do'), 'do')


# In[13]:


s='swiming'
def verbing(s):
    #print(s[-3:])
    if len(s)>3:
        if s[-3:] =='ing':
            s=s+'ly'
            return s
        else:   
            s=s+'ing'
            return s
            
    else:
        return s
verbing(s)    
    


# In[14]:


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
#def not_bad(s):
 # # +++your code here+++
  #return

#print ('not_bad')
  #test(not_bad('This movie is not so bad'), 'This movie is good')
  #test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  #test(not_bad('This tea is not hot'), 'This tea is not hot')
  #test(not_bad("It's bad yet not"), "It's bad yet not")

#str = "this is string example....wow!!!"
#print (str.split( ))
#print (str.split('i',1))
#print (str.split('w'))


# In[84]:


#s='This dinner is not that bad!'
s='This movie is not so bad'
#s='This tea is not hot'
#s="It's bad yet not"
def not_bad(s):
    f=s.find('not')
    #print(f)
    s1=''
    f1=s.find('bad')
    if f1>f:
        #print(f1)
        if f != -1 and f1 != -1:
            f1=f1+3
            s1=s1 + s[0:f]+'good'+s[f1:]
            #print("Hello {} hello {}".format(str1, str2))

            return print("'{}'".format(s1))
    else:
        return s
    
    
    
    
    
    
not_bad(s)    
    


# In[116]:


s='This dinner is not that bad!'
def not_bad(s):
    f=s.find('not')
    s1=''
    f1=s.find('bad')
    if f1>f:
        if f != -1 and f1 != -1:
            f1=f1+3
            s1=s1 + s[0:f]+'good'+s[f1:]
            return print("'{}'".format(s1))
    else:
        return s

not_bad(s)  


# In[ ]:


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the 4 is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
#def front_back(a, b):
 # +++your code here+++
# return

#print ('front_back')
# test(front_back('abcd', 'xy'), 'abxcdy')
 #test(front_back('abcde', 'xyz'), 'abcxydez')
 #test(front_back('Kitten', 'Donut'), 'KitDontenut')



# In[ ]:


s='abcdefgh'
s1='xywe'

def front_back(s):
    print(s)
    t=len(s)/2
    print(t)
    print(type(t))
    while t !=1:
        t=t/2
        t1=len(s1)
        print(t)
        print(s[0:t]+s1[0:t1])
        
    
    
front_back(s)  


# In[138]:





# In[320]:


print('helo')

''' hash = {}
  hash['word'] = 'garfield'
  hash['count'] = 42
  s = 'I want %(count)d copies of %(word)s' % hash  # %d for int, %s for string
  # 'I want 42 copies of garfield '''


# In[474]:


#f = open('workfile', 'w')
#f.read()
#f.readline()

def wordCount():
    f=open('/Users/akshaykumar/desktop/googlepython/basic/baby1990 2.html','r')
    file_in_list =f.readlines()# read all file give a list of string
    #print(r)
    dicfile={}
    count=1
    for liststr in file_in_list:
        liststr=liststr.split()#split string by space and return list of string 
       # print(liststr)
        
        for element_in_list in liststr:
            #print(element_in_list)
            
            if element_in_list not in dicfile:
                dicfile[element_in_list]=count
                #print('value of dicfile',dicfile)
                
            else:
                for j ,k in dicfile.items():
                    if j==element_in_list:
                        k=k+1
                        #print(k)
                        #count=count+1
                        dicfile[j]=k
    print(dicfile)
    f.close()
    topcount(dicfile)
    
#def topcount(dicfile):
    #print(dicfile)
    #print(type(dicfile))
    
    #print(dicfile.keys())
    #print(type(dicfile.keys()))
    
    #print(dicfile.values())
    #list
    #val=dicfile.values()
    #print(sorted(val))
    #for k,v in dicfile.items():
     #   print(sorted(v))
#     dicnew = {}
#     for k,v in dicfile.items():
#         dicnew[v]=k
#         print(k,v)
        
    
    
   
     #   print(key)
        
        
    
wordCount() 


# In[461]:



# #import sys
# #import re

# #Baby Names exercise

# '''Define the extract_names() function below and change main()
# to call it.

# For writing regex, it's nice to include a copy of the target
# text for inspiration.

# Here's what the html looks like in the baby.html files:
# '''


# In[459]:


# import sys
# import re

# def extract_names('file:///Users/akshaykumar/Desktop/googlepython/babynames/baby1990%202.html'):
#     print('hellO')
    
    
# extract_names()    
    

