class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        dec_int = int(s,2)
        counts = 0
        while dec_int != 1:
            if dec_int % 2 == 0:
                dec_int = dec_int // 2
            else:
                dec_int +=1
            
            counts += 1
        
        return counts
            
