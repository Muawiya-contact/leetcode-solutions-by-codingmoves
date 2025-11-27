# 3381. Maximum Subarray Sum With Length Divisible by K

## 📌 Problem Statement

You are given an integer array `nums` and an integer `k`.

Your task is to **find the maximum sum of a subarray** such that:

- The subarray is **continuous**
- The **length of the subarray is divisible by `k`**

Return the maximum possible sum.

---

## 🧠 Key Observations

- A **subarray** is a continuous portion of an array.
- Valid subarray lengths are:  
  `k, 2k, 3k, ...`
- Brute force checking all subarrays would be too slow for large arrays.
- We use **Prefix Sum + Modulo** to solve the problem efficiently.

---

## 💡 Core Idea (Prefix Sum + Modulo)

### Prefix Sum Definition
```py
prefix[i] = sum of elements from index 0 to i-1
```
