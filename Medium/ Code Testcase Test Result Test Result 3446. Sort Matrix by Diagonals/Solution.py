class Solution:
    def sortMatrix(self, grid):
        n = len(grid)

        # Bottom-left diagonals (including main diagonal) → descending
        for start_row in range(n - 1, -1, -1):
            diagonal = []
            r, c = start_row, 0
            while r < n and c < n:
                diagonal.append(grid[r][c])
                r += 1
                c += 1
            diagonal.sort(reverse=True)  # descending
            r, c, pos = start_row, 0, 0
            while r < n and c < n:
                grid[r][c] = diagonal[pos]
                r += 1
                c += 1
                pos += 1

        # Top-right diagonals → ascending
        for start_col in range(1, n):
            diagonal = []
            r, c = 0, start_col
            while r < n and c < n:
                diagonal.append(grid[r][c])
                r += 1
                c += 1
            diagonal.sort()  # ascending
            r, c, pos = 0, start_col, 0
            while r < n and c < n:
                grid[r][c] = diagonal[pos]
                r += 1
                c += 1
                pos += 1

        return grid
