# 🧩 Leetcode 2411: Smallest Subarrays With Maximum Bitwise OR

## 🔗 Problem Link
[Leetcode 2411 - Smallest Subarrays With Maximum Bitwise OR](https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or)

---

## 📄 Problem Statement

You are given a **0-indexed** array `nums` of length `n`, consisting of non-negative integers.

For **each index `i` (from 0 to n - 1)**, you must determine the **size of the smallest non-empty subarray** starting at `i` such that the **bitwise OR** of that subarray is **equal to the maximum possible bitwise OR** of any subarray starting at `i`.

### 💡 Definitions

- **Subarray**: A **contiguous** (continuous) part of the array.
- **Bitwise OR**: An operation that performs `OR` on each bit of two numbers.  
  For example, `2 | 1 = 3` (binary: `10 | 01 = 11`)

---

## 🧠 Goal

For each index `i` in the array `nums`, find the smallest length of a subarray starting from `i` such that its bitwise OR is the **maximum** possible for any subarray that starts at `i`.

Return the result as an integer array of length `n`.

---

## ✅ Example 1

### Input:
```python
nums = [1, 0, 2, 1, 3]
```
