class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        for i in range(1, n-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i-1]
                continue
            if nums[i-1] < nums[i] > nums[i+1] or nums[i-1] > nums[i] < nums[i+1]:
                result += 1
        return result
