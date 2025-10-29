class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
       
        return int( ((len(bin(n)[2:]))*"1"), 2)
