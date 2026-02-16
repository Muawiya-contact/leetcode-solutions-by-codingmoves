class Solution(object):
    def reverseBits(self, n):
        result = 0
        for _ in range(32):
            result <<= 1          # shift result left
            result |= (n & 1)     # add last bit of n
            n >>= 1               # shift n right
        return result

obj = Solution()
print(obj.reverseBits(43261596))
