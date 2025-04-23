class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        from collections import defaultdict

        # Dictionary to store frequency of each digit sum
        digit_sum_groups = defaultdict(int)

        # Loop through all numbers from 1 to n
        for num in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(num))  # Sum of digits
            digit_sum_groups[digit_sum] += 1           # Count how many numbers fall into this group

        # Find the largest group size
        max_size = max(digit_sum_groups.values())

        # Count how many groups have this max size
        return sum(1 for size in digit_sum_groups.values() if size == max_size)
