class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        
        # Iterate through the array to consider all subarrays of length 3
        for i in range(1, len(nums) - 1):
            # Check if 2 * (first + third) equals second element
            if 2 * (nums[i - 1] + nums[i + 1]) == nums[i]:
                count += 1
        
        return count

# Example usage
nums1 = [1, 2, 1, 4, 1]
nums2 = [1, 1, 1]
nums3 = [2, -7, -6]

solution = Solution()
print(solution.countSubarrays(nums1))  # Output: 1
print(solution.countSubarrays(nums2))  # Output: 0
print(solution.countSubarrays(nums3))  # Output: 0
