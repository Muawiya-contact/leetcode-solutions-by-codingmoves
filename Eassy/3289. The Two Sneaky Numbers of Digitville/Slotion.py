class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        c = Counter(nums)
        r = []
        k = list(c.keys())
        for x in k:
            if c[x] == 2 :
                r.append(x)
            
        return r
        
