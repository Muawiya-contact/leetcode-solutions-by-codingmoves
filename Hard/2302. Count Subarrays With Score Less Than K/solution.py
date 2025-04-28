class Solution(object):
    def countSubarrays(self, nums, k):
        n = len(nums)
        total = 0
        left = 0
        current_sum = 0

        for right in range(n):
            current_sum += nums[right]
            while (current_sum * (right - left + 1)) >= k:
                current_sum -= nums[left]
                left += 1
            total += (right - left + 1)

        return total
