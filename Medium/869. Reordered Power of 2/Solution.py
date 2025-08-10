from itertools import permutations

class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def is_power_of_two(num):
            """Check if a number is a power of 2."""
            return num > 0 and (num & (num - 1)) == 0

        digits = str(n)
        # Generate all unique permutations without leading zero
        for p in set(permutations(digits)):
            if p[0] != '0':  # skip numbers starting with 0
                if is_power_of_two(int(''.join(p))):
                    return True
        return False


# Example usage
sol = Solution()
print(sol.reorderedPowerOf2(124))  # False
print(sol.reorderedPowerOf2(128))  # True
print(sol.reorderedPowerOf2(1))    # True
print(sol.reorderedPowerOf2(144))  # False
