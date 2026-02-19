class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev_count = 0
        curr_count = 1
        result = 0

        for i in range(1,len(s)):
            if s[i] == s[i-1]:
               curr_count += 1

            else:
                result += min(prev_count, curr_count)
                prev_count = curr_count 
                curr_count = 1

        result += min(prev_count, curr_count)
    
        return result
        
