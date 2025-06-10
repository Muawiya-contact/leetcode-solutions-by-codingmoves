from collections import Counter

class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = Counter(s)
        odd_freqs = [v for v in freq.values() if v % 2 == 1]
        even_freqs = [v for v in freq.values() if v % 2 == 0]
        
        return max(odd_freqs) - min(even_freqs)
