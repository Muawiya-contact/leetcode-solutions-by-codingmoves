class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        nums.sort()
        for i in nums:
            if i == original:
                original = 2 * original

        return original
