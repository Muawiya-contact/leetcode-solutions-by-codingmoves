class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 0

        for i in range(len(nums) // 2):
            res = max(res, nums[i] + nums[-1-i])
        
        return res 
