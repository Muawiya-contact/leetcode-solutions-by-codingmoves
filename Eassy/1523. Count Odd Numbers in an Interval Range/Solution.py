class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        import math
        count = 0
        if low %2 != 0:
            count =  math.ceil(((high+1) - (low-1))/2)
        else:
            count =  math.floor(((high+1) - (low))/2)
        return  int(count)
