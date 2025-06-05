# Lexicographically Smallest Equivalent String

**Leetcode Problem ID:** 1061  
**Difficulty:** Medium  
**Topics:** Union-Find, Graph, DFS  
**Status:** ✅ Solved

## Problem Description

You are given two strings `s1` and `s2` of the same length and a string `baseStr`.

We say characters `s1[i]` and `s2[i]` are **equivalent**. This equivalence is transitive, symmetric, and reflexive.

Your task is to return the **lexicographically smallest equivalent string** of `baseStr` using the equivalence information derived from `s1` and `s2`.

---

## Example

### Example 1:
**Input:**
```python
s1 = "parker"
s2 = "morris"
baseStr = "parser"
```
### Output:
```python
"makkek"
```
**Explanation:**
Characters can be grouped as:
- [m, p]
- [a, o]
- [k, r, s]
- [e, i]

Each character in `baseStr` is replaced with the smallest character from its group.

---
## Constraints

- `1 <= s1.length, s2.length, baseStr.length <= 1000`
- `s1.length == s2.length`
- `s1`, `s2`, and `baseStr` consist of **lowercase English letters** only.

---

## Approach

We model the problem using a **graph of equivalent characters** and use **DFS** to find the **lexicographically smallest character** in the equivalence group for each character in `baseStr`.

### Steps:

1. **Build a graph** where each character points to its equivalent characters.
2. For every character in `baseStr`, **perform DFS** to find the smallest lexicographic character in its connected component.
3. Replace the character with the found minimum.
4. Return the final transformed string.

---
### Alternative Approaches
 + A more optimized version can use the Union-Find (Disjoint Set Union) structure to reduce repeated DFS traversals and achieve near O(n) performance.

---





