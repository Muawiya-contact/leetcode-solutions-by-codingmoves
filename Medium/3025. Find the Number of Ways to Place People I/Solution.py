class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: (x[0], -x[1]))
        n = len(points)
        ans = 0
        for i in range(n-1):
            hi = points[i][1]
            lo = float('-inf')
            for j in range(i + 1, n):
                cur = points[j][1]
                if cur > hi: continue
                if cur > lo:
                    ans += 1
                    lo = cur
        return ans
