class Solution(object):
    def minOperations(self, nums):
        s = [0]
        res = 0
        for a in nums:
            while s and s[-1] > a:
                s.pop()
            if not s or s[-1] < a:
                res += 1
                s.append(a)
        return res
