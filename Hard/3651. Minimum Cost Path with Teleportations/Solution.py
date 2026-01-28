class Solution:
    def minCost(self, grid, k):
        n, m = len(grid), len(grid[0])
        
        # 1. Find maximum value in the grid
        max_val = max(max(row) for row in grid)
        
        # dp[i][j] = min cost to reach bottom-right from (i,j)
        dp = [[0] * m for _ in range(n)]
        
        # temp[v] = min cost starting from any cell with value v
        temp = [float('inf')] * (max_val + 1)
        best = [float('inf')] * (max_val + 1)
        
        # Base case: cost at target is 0 (we only pay when ENTERING cells)
        temp[grid[n - 1][m - 1]] = 0
        
        # --- K = 0 (no teleport) initialization ---
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                if i == n - 1 and j == m - 1:
                    continue
                
                down = dp[i + 1][j] + grid[i + 1][j] if i + 1 < n else float('inf')
                right = dp[i][j + 1] + grid[i][j + 1] if j + 1 < m else float('inf')
                
                dp[i][j] = min(down, right)
                
                # Update temp for this cell value
                temp[grid[i][j]] = min(temp[grid[i][j]], dp[i][j])
        
        # --- Teleport layers (K > 0) ---
        for _ in range(k):
            # Build prefix minimum array
            best[0] = temp[0]
            for v in range(1, max_val + 1):
                best[v] = min(best[v - 1], temp[v])
            
            # Update DP table with teleport options
            for i in reversed(range(n)):
                for j in reversed(range(m)):
                    if i == n - 1 and j == m - 1:
                        continue
                    
                    down = dp[i + 1][j] + grid[i + 1][j] if i + 1 < n else float('inf')
                    right = dp[i][j + 1] + grid[i][j + 1] if j + 1 < m else float('inf')
                    walk_cost = min(down, right)
                    
                    # Teleport option
                    teleport_cost = best[grid[i][j]]
                    
                    dp[i][j] = min(walk_cost, teleport_cost)
                    
                    # Update temp for next iteration
                    temp[grid[i][j]] = min(temp[grid[i][j]], dp[i][j])
        
        return dp[0][0]


# Example usage
sol = Solution()

grid1 = [[1,3,3],[2,5,4],[4,3,5]]
k1 = 2
print(sol.minCost(grid1, k1))  # Output: 7

grid2 = [[1,2],[2,3],[3,4]]
k2 = 1
print(sol.minCost(grid2, k2))  # Output: 9
