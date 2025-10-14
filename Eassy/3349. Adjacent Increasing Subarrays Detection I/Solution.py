class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)

        # Function to check if subarray nums[i:i+k] is strictly increasing
        def is_increasing(start):
            for j in range(start, start + k - 1):
                if nums[j] >= nums[j + 1]:
                    return False
            return True

        # Check adjacent subarrays of length k
        for i in range(n - 2 * k + 1):
            if is_increasing(i) and is_increasing(i + k):
                return True

        return False
