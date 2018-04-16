
# coding: utf-8

# In[7]:


class Solution(object):
    def permute(self, num):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(num) == 0: return []
        if len(num) == 1: return [num]
        res = []
        for i in range(len(num)):
            #print 'num[:i]',num[:i]
            #print 'num[i+1:]',num[i+1:]
            #print 'num[:i] + num[i+1:]',num[:i] + num[i+1:]
            for j in self.permute(num[:i] + num[i+1:]):
                #print '[num[i]]:',[num[i]]
                #print 'j',j
                res.append([num[i]] + j)
        return res
            
if __name__=="__main__":
    nums = [1,2,3]
    print (Solution().permute(nums) )   

