class Solution(object):
    def canPartitionGrid(self, grid):
        
        m = len(grid)
        n = len(grid[0])
        
        total = sum(sum(row) for row in grid)
        
        # If total sum is odd → impossible
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        # Horizontal cuts
        curr = 0
        for i in range(m-1):
            curr += sum(grid[i])
            if curr == target:
                return True
        
        # Vertical cuts
        curr = 0
        for j in range(n-1):
            col_sum = 0
            for i in range(m):
                col_sum += grid[i][j]
            
            curr += col_sum
            
            if curr == target:
                return True
        
        return False
