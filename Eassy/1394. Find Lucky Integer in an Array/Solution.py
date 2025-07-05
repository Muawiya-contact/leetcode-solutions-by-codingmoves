from collections import Counter
class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        c = Counter(arr)
        r = []
        for i in arr:
            if c[i] == i:
                r.append(i)

        if not r:   # if r is empty
            return -1
        else:
            return max(r)
        
