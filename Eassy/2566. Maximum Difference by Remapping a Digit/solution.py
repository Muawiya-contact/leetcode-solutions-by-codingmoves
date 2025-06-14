class Solution:
    def minMaxDifference(self, num):
        s = str(num)

        # For max: find the first digit not 9 and replace all its instances with 9
        for ch in s:
            if ch != '9':
                max_num = int(s.replace(ch, '9'))
                print(max_num)
                break
            else:
                max_num = num

        # For min: find the first digit not 0 and replace all its instances with 0
        for ch in s:
            if ch != '0':
                min_num = int(s.replace(ch, '0'))
                print(min_num)
                break
            else:
                min_num = num

        return max_num - min_num

obj = Solution()
print(obj.minMaxDifference(232333))
