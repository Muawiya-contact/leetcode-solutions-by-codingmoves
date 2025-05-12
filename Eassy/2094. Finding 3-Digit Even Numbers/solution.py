from collections import Counter

class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        count = Counter(digits)
        result = set()
        
        # Loop over all possible 3-digit numbers
        for num in range(100, 1000):
            if num % 2 != 0:
                continue  # skip odd numbers

            temp = Counter([int(d) for d in str(num)])
            if all(temp[d] <= count[d] for d in temp):
                result.add(num)

        return sorted(result)
