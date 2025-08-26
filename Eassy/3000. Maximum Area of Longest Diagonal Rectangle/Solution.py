class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        max_diag = -1   # longest diagonal^2 found so far
        max_area = -1   # corresponding max area
        
        for l, w in dimensions:
            diag_sq = l*l + w*w   # squared diagonal
            area = l * w
            if diag_sq > max_diag or (diag_sq == max_diag and area > max_area):
                max_diag = diag_sq
                max_area = area
                
        return max_area
