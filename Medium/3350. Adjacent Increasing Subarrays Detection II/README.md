# 🚀 LeetCode 3350 — Adjacent Increasing Subarrays Detection II

## 📘 Problem Statement

Given an integer array `nums`, find the **maximum value of `k`** for which there exist two **adjacent subarrays** of length `k` each that are **strictly increasing**.

Formally, there exist indices `a` and `b` (`a < b`, `b = a + k`) such that:
- Both subarrays `nums[a..a+k-1]` and `nums[b..b+k-1]` are strictly increasing.
- Return the **maximum** such `k`.

A subarray is a contiguous non-empty sequence of elements within an array.

---

## 🧠 Example 1

**Input**
```python
nums = [2,5,7,8,9,2,3,4,3,1]
```
