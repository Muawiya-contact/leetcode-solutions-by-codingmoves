from typing import List

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # Use cross-product-based area (robust and simple)
        def area(a, b, c):
            return abs((b[0]-a[0])*(c[1]-a[1]) - (c[0]-a[0])*(b[1]-a[1])) / 2.0
        
        n = len(points)
        max_area = 0.0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    max_area = max(max_area, area(points[i], points[j], points[k]))
        return max_area
