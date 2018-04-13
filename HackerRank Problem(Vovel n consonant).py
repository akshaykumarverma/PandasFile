
# coding: utf-8

# In[1]:


print('hello')


# In[78]:


import sys


def Test():
    Sample_input = 'BANANA'
    liscon = []
    lisvowel = []
    t = ''
    i = 0
    j = 0
    # print(len(Sample_input))
    i1 = 0

    while (i <= len(Sample_input) - 1):
        s = Sample_input[i]
        i1 = i
        count = 0
        print(s[0])

        j = i
        while (j <= len(Sample_input) - 1):
            if count == 0:
                if s[0] == 'A' and 'E' and 'I' and 'O' and 'U':
                    lisvowel.append(s)
                    count = count + 1
                else:
                    liscon.append(s)
                    count = count + 1
            j = i + 1
            if j < len(Sample_input):
                if s[0] == 'A' and 'E' and 'I' and 'O' and 'U':
                    s = s + Sample_input[j]
                    lisvowel.append(s)
                    i = j
                else:
                    s = s + Sample_input[j]
                    liscon.append(s)
                    i = j
        i = i1 + 1
   # print('===liscon===', liscon)
   # print('===lisvowel===', lisvowel)
    calculate(liscon,lisvowel,Sample_input)
    
def calculate(liscon,lisvowel,Sample_input):
    newlisvowel = []
    newliscon= []
    diccon={}
    dicvowel={}
    for i  in liscon:
        if i not in newliscon:
            newliscon.append(i)
            #print(i)
            diccon[i]=Sample_input.find(i)
            
            
    
          
    for i  in lisvowel:
        if i not in newlisvowel:
            newlisvowel.append(i)
            dicvowel[i]=Sample_input.find(i)
    print(newlisvowel)
    print(newliscon)
    
    print(dicvowel)
    
    print(diccon)
    
     
    
     
    
    
        
        
    
    
    


Test()


# In[184]:


string='BANANA'
sub_string='NA'
def count_substring(string, sub_string):
    count=0
    #print(len(string),len(sub_string))
    for i in range(0, len(string)-len(sub_string)+1):
        if string[i] == sub_string[0]:
            flag=1
            for j in range (0, len(sub_string)):
                if string[i+j] != sub_string[j]:
                    flag=0
                    break
            if flag==1:
                count += 1
    return count        
count_substring(string,sub_string) 

