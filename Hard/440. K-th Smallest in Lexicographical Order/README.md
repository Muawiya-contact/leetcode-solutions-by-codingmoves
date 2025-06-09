# 440. K-th Smallest in Lexicographical Order

## 🧩 Problem Statement

Given two integers `n` and `k`, return the **k-th smallest integer** in the range `[1, n]` when all numbers are sorted in **lexicographical (dictionary) order**.

### 🧠 Lexicographical Order?

Lexicographical order means comparing numbers as **strings**. For example:

### Input: 
```python
n = 13
Lex Order: [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## 🧪 Example

### Example 1:
### Input:
```text
n = 13
k = 2
```
### Output: 
```text
10
```
---
### ✅ Constraints
  + `1 <= k <= n <= 10^9`
---
### ✅ Optimized Solution (Prefix Tree Counting)
Key Concepts:
  + View numbers as a trie/prefix tree.
  
  + At each node (prefix), count how many numbers fall under it.
  
  + Use this to either:
  
    + Skip to next prefix (`prefix + 1`), or
    
    + Dive deeper (`prefix * 10`)

---
### ⏱️ Time & Space Complexity
  + Aspect	Complexity
  + Time Complexity	O(log n × log n)
  + Space Complexity	O(1)
---
### 🏆 Why This Works
  + Lexicographical numbers form a virtual trie (prefix tree).
  
  + Instead of storing all numbers, we count prefixes.
  
  + Efficient even when n is up to 1 billion.

---
### 🤝 Contributed By
  + @Coding_Moves – LeetCode & GitHub Learning Journey 💻🚀
  
  + Built as part of structured practice in Lexicographical Algorithms.
  
---

