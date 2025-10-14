# 🧩 LeetCode 3349 — Adjacent Increasing Subarrays Detection I

## 📘 Problem Description

Given an array `nums` of `n` integers and an integer `k`, determine whether there exist **two adjacent subarrays** of length `k` such that both are **strictly increasing**.

Formally, find indices `a` and `b` (`a < b`) such that:

- Both subarrays `nums[a..a + k - 1]` and `nums[b..b + k - 1]` are strictly increasing.
- The subarrays are **adjacent**, meaning `b = a + k`.

Return `true` if such subarrays exist, otherwise return `false`.

---

## 🧠 Example 1

**Input:**
```python
nums = [2,5,7,8,9,2,3,4,3,1]
k = 3
```
