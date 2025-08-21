class Solution:
    def numSubmat(self, mat):
        n, m = len(mat), len(mat[0])
        newmat = [[0] * m for _ in range(n)]

        # Precompute consecutive ones to the right
        for i in range(n):
            newmat[i][m-1] = 1 if mat[i][m-1] == 1 else 0
            for j in range(m-2, -1, -1):
                newmat[i][j] = 0 if mat[i][j] == 0 else newmat[i][j+1] + 1

        count = 0
        for i in range(n):
            for j in range(m):
                minwidth = newmat[i][j]
                for d in range(i, n):
                    if newmat[d][j] == 0:
                        break
                    minwidth = min(minwidth, newmat[d][j])
                    count += minwidth
        return count


# Example usage:
mat = [[1,0,1],
       [1,1,0],
       [1,1,0]]
print(Solution().numSubmat(mat))  # Output: 13
