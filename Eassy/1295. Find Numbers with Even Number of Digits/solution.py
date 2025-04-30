class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in nums:
            j = str(i)
            if len(j) % 2 == 0:
                count += 1
                
        return count
        
obj = Solution()
print(obj.findNumbers([1,22,3,33,33]))
