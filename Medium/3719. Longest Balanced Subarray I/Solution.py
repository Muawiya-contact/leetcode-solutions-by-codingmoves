class Solution(object):
    def longestBalanced(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        max_len = 0

        for i in range(n):
            evens = set()
            odds = set()
            for j in range(i, n):
                if nums[j] % 2 == 0:
                    evens.add(nums[j])
                else:
                    odds.add(nums[j])
                if len(evens) == len(odds):
                    max_len = max(max_len, j - i + 1)
        return max_len
        
