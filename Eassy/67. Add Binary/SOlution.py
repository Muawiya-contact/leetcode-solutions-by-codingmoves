class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Convert Binary String to decimal int
        a = int(a,2)
        b = int(b,2)

        # bin() returns sting with '0b1
        s = bin(a+b)

        return s[2:] # Remove '0b' and return the binay sum
