class Solution(object):
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """

        # Step 1: Count how many numbers have each remainder
        remainder_count = {}  # dictionary to store count of each remainder

        for num in nums:
            # we use ((num % value) + value) % value to handle negative numbers properly
            r = ((num % value) + value) % value
            remainder_count[r] = remainder_count.get(r, 0) + 1

        # Step 2: Start checking numbers from 0, 1, 2, 3, ...
        x = 0
        while True:
            remainder = x % value
            # if we have a number available with this remainder
            if remainder_count.get(remainder, 0) > 0:
                # use one of them (like marking it used)
                remainder_count[remainder] -= 1
                x += 1
            else:
                # if not found, then x is the smallest missing number (MEX)
                return x
