from collections import Counter

class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(nums)
        result = []

        for i in range(n - k + 1):
            sub = nums[i:i + k]  # current subarray
            freq = Counter(sub)  # count frequencies

            # Sort by frequency desc, then value desc
            sorted_items = sorted(freq.items(), key=lambda p: (p[1], p[0]), reverse=True)

            # Take only top x numbers
            top_x = set(num for num, _ in sorted_items[:x])

            # Sum up all elements in sub that are in top_x
            total = sum(num for num in sub if num in top_x)

            result.append(total)

        return result
