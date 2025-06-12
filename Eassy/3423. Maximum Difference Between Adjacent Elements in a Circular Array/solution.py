class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxa = abs(nums[0] - nums[-1])
        for i in range(n-1):
            maxa = max(maxa,abs(nums[i] - nums[i+1]))
        
        return maxa    
        
obj = Solution() 
print(obj.maxAdjacentDistance([1,2,3,4,5]))
