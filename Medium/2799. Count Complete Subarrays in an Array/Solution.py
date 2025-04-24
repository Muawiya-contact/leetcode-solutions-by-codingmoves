class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_distinct = len(set(nums))  # Step 1: total distinct numbers in the full array
        n = len(nums)
        count = 0
        
        # Step 2: check all subarrays
        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])  # build the current subarray and track unique elements
                if len(seen) == total_distinct:
                    count += 1  # found a complete subarray
        return count
