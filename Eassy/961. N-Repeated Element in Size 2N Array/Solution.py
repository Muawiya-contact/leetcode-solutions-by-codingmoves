class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        
        n = len(nums) // 2  # integer division
        num_count = Counter(nums)
        
        for k, v in num_count.items():
            if v == n:
                return k  # return the element, not the count
        
        return False

        
