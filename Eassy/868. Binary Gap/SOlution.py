class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        max_dis = 0
        prev_p = 0
        j = str(bin(n)[2:])
        print(j)
        for i in range(0,len(j)):
            if int(j[i]) == 1:
                cur_p = i 
                cur_d = cur_p - prev_p
                max_dis = max(cur_d,max_dis)
                prev_p = cur_p
                
        return max_dis
