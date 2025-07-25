class Solution:
    def maxSum(self, nums: List[int]) -> int:
        return max(max(nums), sum(num for num in set(nums) if num > 0) or -inf)
