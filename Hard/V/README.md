# 3197. Find the Minimum Area to Cover All Ones II

**Difficulty:** Hard  
**Problem Type:** Grid, Geometry, DP/Optimization

## Problem Statement
You are given a 2D binary array `grid`. Find **three non-overlapping** axis-aligned rectangles, each with **non-zero area**, such that **every** cell containing `1` lies **inside at least one** of these rectangles. Rectangles may **touch** (share edges or corners) but may **not overlap in area**.

Return the **minimum possible sum of the areas** of these three rectangles.

## Notes
- Rectangles must have horizontal and vertical sides.
- "Non-overlapping" means their interiors do not intersect (touching is allowed).
- Each rectangle’s area must be ≥ 1.

## Examples

### Example 1
**Input:**  
`grid = [[1,0,1],[1,1,1]]`

**Output:**  
`5`

**Explanation:**  
- Rectangle A covers ones at `(0,0)` and `(1,0)` → area = 2  
- Rectangle B covers ones at `(0,2)` and `(1,2)` → area = 2  
- Rectangle C covers one at `(1,1)` → area = 1  
- Total = 2 + 2 + 1 = **5**

### Example 2
**Input:**  
`grid = [[1,0,1,0],[0,1,0,1]]`

**Output:**  
`5`

**Explanation:**  
- Rectangle A covers ones at `(0,0)` and `(0,2)` → area = 3  
- Rectangle B covers one at `(1,1)` → area = 1  
- Rectangle C covers one at `(1,3)` → area = 1  
- Total = 3 + 1 + 1 = **5**

## Constraints
- `1 <= grid.length, grid[i].length <= 30`
- `grid[i][j] ∈ {0, 1}`
- The input contains **at least three** cells with value `1`.
