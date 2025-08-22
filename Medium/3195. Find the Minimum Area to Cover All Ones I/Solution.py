class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        h_min = -1
        h_max = -1
        v_min = -1
        v_max = -1

        for i in range(len(grid)):
            if 1 in grid[i]:
                print("h_min", i)
                h_min = i
                h_max = i
                break

        for i in range(len(grid)-1,-1,-1):
            if 1 in grid[i]:
                print("h_max", i)
                h_max = i
                break

        escape = False
        for i in range(len(grid[0])):  
            if escape:
                break
            for j in range(len(grid)):
                if grid[j][i] == 1:
                    v_min = i
                    v_max = i
                    escape = True
                    break

        escape = False
        for i in range(len(grid[0])-1,-1,-1):
            if escape:
                break
            for j in range(len(grid)):
                if grid[j][i] == 1:
                    v_max = i
                    escape = True
                    break

        #print(v_min, v_max, h_min, h_max)

        if v_min == -1:
            return 0
        return (v_max - v_min + 1) * (h_max - h_min + 1)
 
