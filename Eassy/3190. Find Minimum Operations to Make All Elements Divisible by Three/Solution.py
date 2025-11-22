class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0  # counts steps
        for i in nums:
            if i % 3 == 0:
                continue
            else:
                i -= i % 3 
                count += 1
        return count
        
