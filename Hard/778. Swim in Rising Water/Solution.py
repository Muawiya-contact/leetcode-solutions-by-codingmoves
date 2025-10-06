from collections import deque

class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        
        # Function to check if we can reach the end at time t
        def canReach(t):
            if grid[0][0] > t:
                return False
            
            visited = [[False]*n for _ in range(n)]
            queue = deque([(0, 0)])
            visited[0][0] = True
            
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            
            while queue:
                x, y = queue.popleft()
                if x == n-1 and y == n-1:
                    return True
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                        if grid[nx][ny] <= t:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
            return False
        
        # Binary search on time (water level)
        low = max(grid[0][0], grid[n-1][n-1])
        high = n * n - 1
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if canReach(mid):
                ans = mid
                high = mid - 1  # try smaller time
            else:
                low = mid + 1   # need more water
        
        return ans
