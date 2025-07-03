class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        word = "a"
        while len(word) < k:
            next_part = ''.join(
                chr((ord(c) - ord('a')+1) % 26 + ord('a')) for c in word
            )
            word += next_part
        return word[k - 1]        
