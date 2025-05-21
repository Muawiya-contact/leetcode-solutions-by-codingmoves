class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        zero_in_first_row = any(matrix[0][j] == 0 for j in range(cols))
        zero_in_first_col = any(matrix[i][0] == 0 for i in range(rows))

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
      
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if zero_in_first_row:
            for j in range(cols):
                matrix[0][j] = 0

        if zero_in_first_col:
            for i in range(rows):
                matrix[i][0] = 0                  

