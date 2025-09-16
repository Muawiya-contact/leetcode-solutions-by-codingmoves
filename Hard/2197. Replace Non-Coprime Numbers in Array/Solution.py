
from fractions import gcd   # Python 2

class Solution(object):
    def replaceNonCoprimes(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []

        for num in nums:
            stack.append(num)

            # Keep merging while last two are non-coprime
            while len(stack) > 1:
                a = stack[-1]
                b = stack[-2]
                g = gcd(a, b)

                if g > 1:  # non-coprime
                    lcm = (a * b) // g
                    stack.pop()
                    stack.pop()
                    stack.append(lcm)
                else:
                    break

        return stack
