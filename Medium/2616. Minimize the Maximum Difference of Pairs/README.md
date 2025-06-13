# 🧠 Leetcode 2616 - Minimize the Maximum Difference of Pairs

## 📝 Problem Statement

Given a 0-indexed integer array `nums` and an integer `p`, your task is to form `p` pairs of elements such that:

- No index is used in more than one pair.
- The **maximum difference** among all selected pairs is **minimized**.

For any pair `(i, j)`, the **difference** is calculated as:  
`|nums[i] - nums[j]|`

Return the **minimum possible value of the maximum difference** among all `p` pairs.

---

## 📌 Example

### Input
```python
nums = [10,1,2,7,1,3], p = 2
```
### Output
```
6
```

### Explanation
  + One optimal selection of pairs:
  
    - Pair 1: (1, 4) → |1 - 1| = 0
    
    - Pair 2: (2, 5) → |2 - 3| = 1
  
  + The maximum difference is `max(0, 1) = 1`, which is minimal.

  ---
  ### 👨‍💻 Author
Built with ❤️ by Muawiya (@Coding_Moves)

---
