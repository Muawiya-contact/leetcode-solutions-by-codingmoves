# 🚀 Longest Subsequence Repeated k Times (LeetCode 2014)

## 🧠 Problem Statement

You are given a string `s` and an integer `k`. Your task is to **find the longest subsequence** such that when it is **repeated `k` times**, the resulting string is still a subsequence of `s`.

- A subsequence can be formed by deleting some (or no) characters without changing the order of the rest.
- The returned subsequence should be:
  - As **long** as possible.
  - If multiple answers exist, choose the **lexicographically largest** one.

---

## 🧩 Examples

### Example 1:
### Input: 
```python
s = "letsleetcode", k = 2
```
### Output:
```python
"let"
```

---

## 🔍 Approach Summary

This solution combines **Binary Search**, **DFS**, and a **Next-Character Lookup Table** to efficiently find the longest subsequence repeated `k` times.

### ✅ Key Techniques Used:
- **Next Position Table:** Precomputes where each character appears next in `s` to allow O(1) lookups.
- **Binary Search:** Determines the max length of the repeated subsequence.
- **DFS (Depth-First Search):** Explores lexicographically larger candidates first.
- **Greedy Pruning:** Skips invalid branches early using a feasibility check (`canExtend()`).

---

## 📦 Components

### 1. `nextPos` Table
A `nextPos[i][c]` lookup tells us the **next index ≥ i** in `s` where character `c` occurs.  
This helps us quickly jump through `s` while validating subsequences.

### 2. Binary Search
Searches for the **maximum length** of a possible subsequence that can be repeated `k` times.

### 3. DFS + Pruning
Tries to build strings from `'z'` to `'a'`, level-by-level.  
At each level, it checks if the current partial path (when repeated) can be a subsequence.

### 4. `canExtend()` Checker
Simulates whether `path * K` can be a subsequence of `s` using the `nextPos` table.

---

## 🧮 Time & Space Complexity

| Operation                | Complexity        |
|-------------------------|-------------------|
| Preprocessing `nextPos` | O(n * 26)         |
| DFS Search              | O(26^L) (pruned)  |
| Subsequence Check       | O(L * K) per try  |
| Overall Efficiency      | Optimized for `n ≤ 2000` |

---

## ✅ Output

Returns a string:
- The **longest subsequence** that can be repeated `k` times
- Or `""` if no such subsequence exists

---

## 🛠️ Language

- **Python 3**
- Uses built-in libraries only (`ord`, `chr`, list manipulations)

---

## 🧠 Credits

Algorithm designed using concepts from:
- Lexicographical ordering
- Efficient subsequence testing
- Combinatorial pruning using DFS + Binary Search

---

