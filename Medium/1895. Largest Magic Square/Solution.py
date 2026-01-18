class Solution:
    def largestMagicSquare(self, grid):
        m, n = len(grid), len(grid[0])

        # Prefix sums
        row = [[0]*(n+1) for _ in range(m)]
        col = [[0]*n for _ in range(m+1)]
        diag = [[0]*(n+1) for _ in range(m+1)]
        anti = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                row[i][j+1] = row[i][j] + grid[i][j]
                col[i+1][j] = col[i][j] + grid[i][j]
                diag[i+1][j+1] = diag[i][j] + grid[i][j]
                anti[i+1][j] = anti[i][j+1] + grid[i][j]

        max_k = min(m, n)

        for k in range(max_k, 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    target = row[i][j+k] - row[i][j]

                    # check rows
                    if any(row[i+r][j+k] - row[i+r][j] != target for r in range(k)):
                        continue

                    # check columns
                    if any(col[i+k][j+c] - col[i][j+c] != target for c in range(k)):
                        continue

                    # check diagonals
                    if diag[i+k][j+k] - diag[i][j] != target:
                        continue

                    if anti[i+k][j] - anti[i][j+k] != target:
                        continue

                    return k

        return 1
