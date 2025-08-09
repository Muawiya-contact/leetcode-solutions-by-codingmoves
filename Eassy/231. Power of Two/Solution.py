class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        l = [2**x for x in range(0,32)]
        if n in l:
            return True
        return False
        
