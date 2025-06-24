# LeetCode 2200 - Find All K-Distant Indices in an Array

**Difficulty:** Easy  
**Topic:** Arrays, Math  
**Link:** [LeetCode Problem 2200](https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/)

---

## 🧠 Problem Statement

You are given a **0-indexed integer array** `nums` and two integers `key` and `k`.

An index `i` is called a **k-distant index** if there exists at least one index `j` such that:

- `|i - j| <= k`
- `nums[j] == key`

Return a list of all k-distant indices sorted in increasing order.

---

## ✅ Example 1

```text
Input: nums = [3,4,9,1,3,9,5], key = 9, k = 1  
Output: [1,2,3,4,5,6]

Explanation:
- `nums[2] == 9` → valid indices: 1, 2, 3
- `nums[5] == 9` → valid indices: 4, 5, 6
- Combined result: [1, 2, 3, 4, 5, 6]
```
---
### 🔍 Approach
  + Find all indices where `nums[j] == key`.
  
  + For each such `j`, add all indices `i` within distance `k` to a `result` set.
  
  + Convert the set to a sorted
  + list and return it.
---
