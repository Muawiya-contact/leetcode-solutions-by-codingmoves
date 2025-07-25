# 3487. Maximum Unique Subarray Sum After Deletion

## 🧩 Problem Statement

You are given an integer array `nums`.

You are allowed to delete **any number of elements** from `nums` without making it empty. After performing the deletions, select a **subarray** of `nums` such that:

- All elements in the subarray are **unique**.
- The subarray is **contiguous**.
- The **sum of the elements** in the subarray is **maximized**.

Return the **maximum sum** of such a subarray.

---

## 🧪 Examples

### Example 1
**Input:**
```python
nums = [1, 2, 3, 4, 5]
```
**Output:**
```python
15
```

**Explanation:**  
Select the entire array. All elements are unique. Sum = 1+2+3+4+5 = 15

---
