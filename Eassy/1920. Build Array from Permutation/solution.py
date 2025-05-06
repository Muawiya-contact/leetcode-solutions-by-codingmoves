class Solution(object):
    def buildArray(self, nums):
        ans = []
        for i in range(0, len(nums)):
            ans.append(nums[nums[i]])  # appending value at the index nums[i]
        return ans
