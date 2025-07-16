from itertools import groupby

class Solution:
    def maximumLength(self, a):
        def f(v):
            return v & 1
        q = sum(map(f,a))
        return max(q,len(a)-q,len(list(groupby(a,f))))    
       
