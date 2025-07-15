class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        if len(word) < 3:
            return False
        v = set('aeiouAEIOU')
        if not all(i.isalnum() for i in word):
            return False
        has_v = any(i in v for i in word)
        has_c = any(i.isalpha() and i not in v for i in word)
        return has_v and has_c
obj = Solution()
print(obj.isValid("UuE6"))
