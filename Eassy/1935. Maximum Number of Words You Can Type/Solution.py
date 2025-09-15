class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        broken = set(brokenLetters)
        words = text.split()

        count = 0
        for word in words:
            if not any(ch in broken for ch in word):
                count += 1
        return count
        
