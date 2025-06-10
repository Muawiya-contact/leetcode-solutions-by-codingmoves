# LeetCode Problem: 3442. Maximum Difference Between Even and Odd Frequency I

## 🧠 Problem Statement

You are given a string `s` consisting of lowercase English letters.  
Your task is to find the **maximum difference** `diff = a1 - a2` between the frequency of characters `a1` and `a2` such that:

- `a1` has an **odd frequency** in the string.
- `a2` has an **even frequency** in the string.

Return this **maximum difference**.

---

### ✅ Constraints:

- `3 <= s.length <= 100`
- `s` consists only of lowercase English letters.
- `s` contains **at least one character with an odd frequency** and **one with an even frequency**.

---

## 💡 Examples

### Example 1:

### Input: 
```python
s = "aaaaabbc"
```
### Output: 
```
3
```
### Explanation:

  + `'a'` appears 5 times (odd)
  
  + `'b'` appears 2 times (even)
  
  + Maximum difference = 5 - 2 = 3

  ---

## 🧮 Solution Overview

1. Count the frequency of each character using `collections.Counter`.
2. Filter out frequencies that are **odd** and **even**.
3. Return the difference between:
   - The **maximum** odd frequency
   - The **minimum** even frequency

---
### ✨ Credit
Prepared by: Muawiya (Coding Moves)
Project Type: LeetCode Problem Solution
Language: Python

---
