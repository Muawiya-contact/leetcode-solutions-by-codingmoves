class Solution(object):
    def maxIncreasingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0

        # Left array: length of increasing run ending at i
        left = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                left[i] = left[i - 1] + 1

        # Right array: length of increasing run starting at i
        right = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                right[i] = right[i + 1] + 1

        # Check boundary between i and i+1
        max_k = 0
        for i in range(n - 1):
            # Two adjacent increasing subarrays split at i | i+1
            k = min(left[i], right[i + 1])
            max_k = max(max_k, k)

        return max_k
