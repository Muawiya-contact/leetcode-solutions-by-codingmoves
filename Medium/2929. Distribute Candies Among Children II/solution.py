class Solution(object):
    def distributeCandies(self, n, limit):
        """
        :type n: int
        :type limit: int
        :rtype: int
        """
        total = 0
        for a in range(min(n,limit)+1):
            remaining = n-a
            lower = max(0,remaining - limit)
            upper = min(limit, remaining)
            total += max(0,upper - lower +1)
        return total    
