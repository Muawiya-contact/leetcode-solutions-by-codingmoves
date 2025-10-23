class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while len(s) > 2:
            r_s = ""  # reset for each new round
            for i in range(len(s) - 1):
                r_s += str((int(s[i]) + int(s[i + 1])) % 10)
            s = r_s  # update s to new string

        return s[0] == s[1]


obj = Solution()
print(obj.hasSameDigits("3902"))   # True
print(obj.hasSameDigits("34789"))  # False
