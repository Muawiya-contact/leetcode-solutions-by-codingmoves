# 3201. Find the Maximum Length of Valid Subsequence I

## 🧠 Problem Statement

You are given an integer array `nums`.  
A subsequence `sub` of `nums` with length `x` is called **valid** if it satisfies:

```python
(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2
```

Return the length of the **longest valid subsequence** of `nums`.

A **subsequence** is a sequence derived by removing some (or no) elements, without changing the order of remaining elements.

---

## ✅ Examples

### Example 1:
**Input:**  
`nums = [1, 2, 3, 4]`  
**Output:** `4`  
**Explanation:**  
All adjacent sums are odd → valid.

---

### Example 2:
**Input:**  
`nums = [1, 2, 1, 2, 1, 2]`  
**Output:** `6`  
**Explanation:**  
Alternating odd-even gives consistent `(odd + even) % 2 = 1`

---

### Example 3:
**Input:**  
`nums = [1, 3]`  
**Output:** `2`  
**Explanation:**  
1 + 3 = 4 → even → valid

---

## 🧠 Approach & Intuition

The sum of two numbers is:
- **Even** if both are **even** or both are **odd**
- **Odd** if one is even and the other is odd

So, a valid subsequence must either:
1. Have all elements of the same parity (all even or all odd)
2. Alternate strictly between odd and even (or vice versa)

---

## ⏱️ Time & Space Complexity
+ Time Complexity: `O(n)`

+ Space Complexity: `O(n)` (due to groupby list)
  
---
## 📌 Constraints
+ `2 <= nums.length <= 2 * 10^5`

+ `1 <= nums[i] <= 10^7`

---
## 🔍 Tags
+ Greedy

+ Bit Manipulation

+ Parity Logic

+ Grouping

----
