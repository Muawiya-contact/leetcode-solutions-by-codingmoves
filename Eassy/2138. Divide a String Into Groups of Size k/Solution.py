class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        l = len(s)
        r =[]
        if l % k == 0:
            for i in range(0,l,k):
                r.append(s[i:i+k])
        else:
            for i in range(0,l,k):    
                r.append(s[i:i+k] + fill * (i+k-l))    
        return r            

obj = Solution()
print(obj.divideString("abcdefghi", 2,"x"))  
