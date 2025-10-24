class Solution(object):
    def nextBeautifulNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def is_numerically_balanced(num):
            s = str(num)
            for d in set(s):
                if s.count(d) != int(d):
                    return False
            return True

        n += 1
        while True:
            if is_numerically_balanced(n):
                return n
            n += 1


