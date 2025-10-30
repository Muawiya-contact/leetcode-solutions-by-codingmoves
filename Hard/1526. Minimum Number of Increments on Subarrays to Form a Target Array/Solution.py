class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        res = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                res += target[i] - target[i -1]
        return res
        
