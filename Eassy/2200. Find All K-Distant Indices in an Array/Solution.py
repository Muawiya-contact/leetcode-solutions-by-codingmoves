class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        result = set()
        for j in range(len(nums)):
            if nums[j] == key:
                start = max(0, j-k)
                end = min(len(nums) - 1, j+k)
                for i in range(start, end+1):
                    result.add(i)

        return sorted(result)            
