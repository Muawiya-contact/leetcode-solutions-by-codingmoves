class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        mp = [[0]*26 for _ in range(26)]
        count = 0
        middle = 0
        for s in words:
            x,y = ord(s[0]) - ord('a'), ord(s[1]) - ord('a')
            if mp[y][x] > 0:
                mp[y][x] -= 1
                count += 4
                if x == y:
                    middle -= 1
            else:
                mp[x][y] += 1
                if x == y:
                    middle += 1
        if middle > 0:
            count += 2
        return count                        
