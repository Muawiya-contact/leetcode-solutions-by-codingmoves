class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while len(nums) > 1:
            dp = []
            for i in range(len(nums) - 1):
                dp.append((nums[i] + nums[i + 1]) % 10)  # modulo 10
            nums = dp
        return nums[0]

obj = Solution()
print(obj.triangularSum([1, 2, 3]))  # Output: 6
