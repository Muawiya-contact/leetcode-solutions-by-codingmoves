class Solution(object):
    def constructProductMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        m = len(grid[0])
        MOD = 12345
        
        # Step 1: Compute total product modulo 12345
        total = 1
        for i in range(n):
            for j in range(m):
                total = (total * grid[i][j]) % MOD
        
        # Step 2: Construct product matrix
        p = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] % MOD == 0:
                    p[i][j] = 0
                else:
                    # Using modular inverse to divide modulo MOD
                    p[i][j] = (total * pow(grid[i][j], -1, MOD)) % MOD
        
        return p
