
# coding: utf-8

# In[1]:


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
    print('===liscon===', liscon)
    print('===lisvowel===', lisvowel)
    
    
    


Test()


# In[38]:


string='BANANA'
liscon=['B', 'BA', 'BAN', 'BANA', 'BANAN', 'BANANA', 'N', 'NA', 'NAN', 'NANA', 'N', 'NA']
lisvowel=['A', 'AN', 'ANA', 'ANAN', 'ANANA', 'A', 'AN', 'ANA', 'A']
for sub_string in lisvowel:
    print(sub_string)
    count=0
    sum=0
    for i in range(0, len(string)-len(sub_string)+1):
         if string[i] == sub_string[0]:
            flag=1
            for j in range (0, len(sub_string)):
                if string[i+j] != sub_string[j]:
                    flag=0
                    break
            if flag==1:
                count += 1
    print(count)
    sum=sum+count
    print('==sum===',sum)
print(sum)

