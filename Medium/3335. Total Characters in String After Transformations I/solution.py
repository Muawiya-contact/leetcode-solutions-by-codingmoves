class Solution(object):
 def lengthAfterTransformations(self, s, t):
        """
        :type s: str
        :type t: int
        :rtype: int
        """
        from collections import Counter

        MOD = 10**9 + 7

        # Initialize frequency map
        freq = [0] * 26 
        print(freq) # 'a' to 'z'
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        for _ in range(t):
            new_freq = [0] * 26
            for i in range(26):
                if i == 25:  # 'z'
                    new_freq[0] += freq[i]  # 'a'
                    new_freq[1] += freq[i]  # 'b'
                else:
                    new_freq[i + 1] += freq[i]
            freq = new_freq

        return sum(freq) % MOD
