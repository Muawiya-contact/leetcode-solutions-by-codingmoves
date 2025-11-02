class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """

        # Step 1: Create the grid
        grid = [[0] * n for _ in range(m)]
        # 0 = empty, 1 = guard, 2 = wall, 3 = guarded

        # Step 2: Mark guards and walls
        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 2

        # Step 3: Define directions (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Step 4: Spread the guards' vision
        for r, c in guards:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Move in this direction until wall or guard or border
                while 0 <= nr < m and 0 <= nc < n and grid[nr][nc] not in (1, 2):
                    # Mark as guarded if empty
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = 3
                    nr += dr
                    nc += dc

        # Step 5: Count unguarded empty cells
        unguarded = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    unguarded += 1

        return unguarded
