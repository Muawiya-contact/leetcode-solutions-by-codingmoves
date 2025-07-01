class Solution(object):
        """
        :type word: str
        :rtype: int
        """
        def possibleStringCount(self,word):
            result = set()
            result.add(word)  # Add the original word as one possibility

            n = len(word)
            i = 0

            while i < n:
                j = i
                while j < n and word[j] == word[i]:
                    j += 1

                group_length = j - i
                if group_length > 1:
                    for k in range(1, group_length):  
                        new_word = word[:i] + word[i] * k + word[j:]  
                        result.add(new_word)

                i = j  # Move to next group

            return len(result)
        
