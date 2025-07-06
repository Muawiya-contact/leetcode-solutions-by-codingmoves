# Leetcode 1865 - Finding Pairs With a Certain Sum

## 🧩 Problem Description

You are given two integer arrays `nums1` and `nums2`. Your task is to implement a data structure that supports two types of operations:

1. **Add a value to an element in `nums2`:**

```python
add(index, val)
```
This operation updates `nums2[index] += val`.
2. **Count pairs with a specific sum:**
```python
count(tot)
```
This returns the number of pairs `(i, j)` such that:
```python
nums1[i] + nums2[j] == tot
```
## 📚 Constraints
+ `1 <= nums1.length <= 1000`
  
+ `1 <= nums2.length <= 10^5`

+ `1 <= nums1[i]`, `nums2[i]`, `val`, `tot <= 10^9`

+ At most `1000` calls to both `add` and `count`.

  ------------------
