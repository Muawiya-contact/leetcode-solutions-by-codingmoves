class Solution(object): 
    def minimizeMax(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        nums.sort()  # Step 1: Sort the array

        def can_form_pairs(max_diff):
            count = 0
            i = 1
            while i < len(nums):
                if nums[i] - nums[i - 1] <= max_diff:
                    count += 1
                    i += 2  # skip the next index
                else:
                    i += 1
            return count >= p

        # Binary search on the max difference
        low, high = 0, nums[-1] - nums[0]
        answer = high

        while low <= high:
            mid = (low + high) // 2
            if can_form_pairs(mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1

        return answer

        
