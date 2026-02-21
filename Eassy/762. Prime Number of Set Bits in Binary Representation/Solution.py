class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        coun = 0
        for i in range(left, right +1):
            i = str(bin(i)[2:])

            if self.isPrime(i.count('1')):
                coun += 1
        return coun
            
    def isPrime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
