# 🎨 LeetCode 1931 - Painting a Grid With Three Different Colors

## 🔗 Problem Link
[LeetCode - 1931. Painting a Grid With Three Different Colors](https://leetcode.com/problems/painting-a-grid-with-three-different-colors/)

## 🧩 Problem Description

You are given two integers `m` and `n` representing the number of rows and columns in a grid.  
You must paint each cell of the `m x n` grid using one of **three colors**: Red, Green, or Blue.

### ❗ Constraints:
- No two adjacent cells (vertically or horizontally) can have the **same color**.
- You must **count** how many such valid ways exist to paint the grid.
- Since the number can be very large, return the result modulo **10⁹ + 7**.

### 🧪 Example:

### Input: 
```
m = 1, n = 2
```
### Output:
```
6
```
### Explanation: 
For each of the 3 choices in the first cell, we have 2 choices for the second.
---

## 🧠 Approach

This solution uses **dynamic programming + state compression** based on column patterns.

### 💡 Key Ideas:

1. **Column-based DP**:
   - Paint the grid column by column.
   - Use `3^m` to enumerate all possible color patterns for a column.
   - Store only valid patterns (no adjacent cells in the column with the same color).

2. **Transition Validity**:
   - Build a compatibility table between valid patterns to ensure adjacent columns don’t have matching colors in the same row.

3. **DP State**:
   - `dp[col][pattern]` = number of ways to fill up to column `col`, ending with `pattern`.

4. **Final Result**:
   - Sum all values in the last column: `sum(dp[n]) % MOD`

---
### 🏁 Time & Space Complexity
+ Time Complexity: `O(n * k^2)` where `k = number of valid patterns ≈ 3^m`

+ Space Complexity: `O(n * k)`

  ---
