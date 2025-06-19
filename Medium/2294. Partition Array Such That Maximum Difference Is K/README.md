# Partition Array Such That Maximum Difference Is K

**LeetCode Problem ID:** 2294  
**Difficulty:** Medium  
**Topic:** Greedy, Sorting  
**Language:** Python  

---

## 🧠 Problem Statement

Given an integer array `nums` and an integer `k`, partition the array into one or more subsequences such that:
- Each element in `nums` appears in exactly one subsequence.
- The difference between the **maximum** and **minimum** values in each subsequence is **at most `k`**.

Return the **minimum number of subsequences** required.

A subsequence is a sequence that can be derived from the array by deleting some (or no) elements without changing the order of the remaining elements.

---

## ✅ Example

### Input:
```python
nums = [3, 6, 1, 2, 5]
k = 2
```
### Output:
```
2
```
### Explanation
You can divide into:

  + `[1, 2, 3]` → max - min = 2
  
  +  `[5, 6]` → max - min = 1

---
### 💡 Approach
  1. Sort the array so that elements are in increasing order.
  
  2. Start from the smallest element and keep adding numbers to the current group as long as the difference between the first number of the group and the current number is ≤ k.
  
  3. If the difference exceeds k, start a new group.
---
### Time Complexity:
  `O(n log n)` due to sorting.

### Space Complexity:
  `O(1)` extra space.
  
----
## ✍️ Author

**Built with ❤️ by [Muawiya @Coding_Moves](https://github.com/Coding-Moves)**






--------------
