class Solution(object):
    def minAbsDiff(self,grid, k):
        m, n = len(grid), len(grid[0])
        ans = []
        for i in range(m - k + 1):
            row = []
            for j in range(n - k + 1):
                vals = sorted(set(
                    grid[i+r][j+c]
                    for r in range(k)
                    for c in range(k)
                ))
                if len(vals) < 2:
                    row.append(0)
                else:
                    row.append(min(vals[x+1] - vals[x] for x in range(len(vals)-1)))
            ans.append(row)
        return ans
