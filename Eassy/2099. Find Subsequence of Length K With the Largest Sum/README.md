# 🧮 2099. Find Subsequence of Length K With the Largest Sum

> Difficulty: Easy  
> Category: Arrays, Greedy  
> Source: [LeetCode 2099](https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/)

## 🧠 Problem Statement

You are given an integer array `nums` and an integer `k`. You want to find a **subsequence** of `nums` of length `k` that has the **largest sum**.

Return any such subsequence as an integer array of length `k`.

A **subsequence** is an array that can be derived from another array by deleting some or no elements **without changing the order** of the remaining elements.

---

## 🧾 Examples

### Example 1:
### Input: 
```python
nums = [2, 1, 3, 3], k = 2
```
### Output:
```python
[3, 3]
```
---

## ✅ Constraints
- `1 <= nums.length <= 1000`
- `-10⁵ <= nums[i] <= 10⁵`
- `1 <= k <= nums.length`

---

## ✅ Solution Approach

### 🔑 Key Idea:
To form the **maximum sum subsequence of length `k`** while maintaining **original order**, we follow this approach:

1. **Store each number along with its index**.
2. **Sort the numbers by value** (descending) and pick top `k`.
3. **Re-sort the top `k` by their original indices** to preserve order.
4. **Extract only the values** for final result.

---
# 🧑‍💻 Author Note
> Maintaining order is key in subsequences. Avoid simply sorting the list — instead, track original indices to ensure the output follows the original array's order.
