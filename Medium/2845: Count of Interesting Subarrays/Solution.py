from collections import defaultdict

class Solution(object):
    def countInterestingSubarrays(self, nums, modulo, k):
        count = 0
        prefix = 0
        freq = defaultdict(int)
        freq[0] = 1  # Base case: empty prefix

        for num in nums:
            # Check if current num is "interesting"
            if num % modulo == k:
                prefix += 1

            # Normalize prefix modulo
            curr_mod = prefix % modulo
            target = (curr_mod - k + modulo) % modulo

            # Count how many times target prefix appeared before
            count += freq[target]

            # Update prefix mod frequency
            freq[curr_mod] += 1

        return count
