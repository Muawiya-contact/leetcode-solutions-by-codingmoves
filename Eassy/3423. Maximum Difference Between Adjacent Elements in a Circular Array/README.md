# 3423. Maximum Difference Between Adjacent Elements in a Circular Array

> **Solved**  
> **Difficulty:** Easy  
> **Topics:** Arrays, Math  
> **Note:** In a circular array, the **first and last elements are adjacent**.

---

## 🧩 Problem Statement

Given a **circular array** `nums`, find the **maximum absolute difference** between **adjacent elements**.

**Important:**  
In a circular array, the **first and last** elements are **also adjacent**.

---

## 🔍 Examples

### Example 1:
### Input:
```python
nums = [1, 2, 4]
```
### Output: 
```python
3
```
### Explanation:
Adjacent differences are: `|1-2|` = `1, |2-4|` = `2, |4-1|` = `3 → max` = `3`
---

## ✅ Constraints

- `2 <= nums.length <= 100`
- `-100 <= nums[i] <= 100`

---

## 🧠 Approach

1. Initialize `max_diff` with the absolute difference between the first and last elements (circular condition).
2. Iterate over the array and calculate absolute differences between consecutive pairs.
3. Update `max_diff` whenever a larger difference is found.

---
### 💡 Why Circular?
In normal arrays, nums[0] and nums[n-1] aren't adjacent. But in circular arrays, this extra connection makes boundary elements relevant for distance calculations
---
