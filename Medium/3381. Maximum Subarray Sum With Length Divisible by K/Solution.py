class Solution(object):
    def maxSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum = 0
        max_sum = float('-inf')

        min_prefix = {}
        min_prefix[0] = 0

        for i, num in enumerate(nums, 1):
            prefix_sum += num
            mod = i % k

            if mod in min_prefix:
                max_sum = max(max_sum, prefix_sum - min_prefix[mod])
                min_prefix[mod] = min(min_prefix[mod], prefix_sum)
            else:
                min_prefix[mod] = prefix_sum

        return max_sum
