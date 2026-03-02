class Solution():
    def minSwaps(self,grid):
        n = len(grid)
        # count trailing zeros for each row
        zeros = []
        for row in grid:
            count = 0
            for j in range(n-1, -1, -1):
                if row[j] == 0: count += 1
                else: break
            zeros.append(count)
        
        swaps = 0
        for i in range(n):
            need = n - 1 - i
            # find nearest row from i downward with enough zeros
            found = -1
            for j in range(i, n):
                if zeros[j] >= need:
                    found = j
                    break
            if found == -1:
                return -1
            # bubble it up
            while found > i:
                zeros[found], zeros[found-1] = zeros[found-1], zeros[found]
                found -= 1
                swaps += 1
        
        return swaps
