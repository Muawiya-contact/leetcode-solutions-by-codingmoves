# LeetCode - 73. Set Matrix Zeroes

## 🔗 Problem Link
[LeetCode Problem 73: Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)

## 🧠 Problem Description

Given an `m x n` integer matrix, if an element is `0`, set its entire row and column to `0` in-place.

### Example 1:
### Input: 
```
matrix = [[1,1,1],[1,0,1],[1,1,1]]
```
### Output: 
```
[[1,0,1],[0,0,0],[1,0,1]]
```
---
## ✅ Constraints

- `m == matrix.length`
- `n == matrix[0].length`
- `1 <= m, n <= 200`
- `-2³¹ <= matrix[i][j] <= 2³¹ - 1`

## 🔍 Follow-up

1. A straightforward solution using O(mn) space is not optimal.
2. A better solution uses O(m + n) space.
3. **Can you solve it in constant space?** ✅

---

## 🚀 Solution Approach (Constant Space)

This optimized approach uses the **first row and first column of the matrix** to keep track of which rows and columns should be zeroed.

### Steps:

1. Check if the **first row** and **first column** originally contain any `0`s.
2. Use the **rest of the matrix** to mark rows and columns that need to be zeroed.
3. Update the matrix based on these markers.
4. Finally, zero out the first row and/or column if needed.

---
## 📊 Complexity Analysis

- **Time Complexity:** O(m × n)
- **Space Complexity:** O(1) (in-place)

---

## 💡 Key Concepts

- Matrix manipulation  
- In-place operations  
- Constant space optimization  
- Flag-based row/column tracking  

---

## ✍️ Author

**Moavia Amir**  
LeetCode Daily Streaker | AI Student | Problem Solver  

🔗 [GitHub - CodingMoves](https://github.com/Muawiya-contact)  
🔗 [YouTube - @Coding_Moves](https://youtube.com/@Coding_Moves)
