from collections import Counter

class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        mp = Counter(s)

        # Get max vowel frequency (0 if no vowel)
        vowel = max((mp[ch] for ch in mp if ch in "aeiou"), default=0)

        # Get max consonant frequency (0 if no consonant)
        consonant = max((mp[ch] for ch in mp if ch not in "aeiou"), default=0)

        return vowel + consonant
