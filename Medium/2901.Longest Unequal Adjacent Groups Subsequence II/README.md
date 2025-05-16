# LeetCode 2901: Longest Unequal Adjacent Groups Subsequence II

## Problem Statement

You are given a string array `words` and an array `groups`, both of length `n`.

A valid subsequence of indices `[i0, i1, ..., ik-1]` (where `k` is the length) must satisfy:

1. For all adjacent indices: `groups[ij] != groups[ij+1]`.
2. The corresponding words must have the **same length** and **Hamming distance = 1**.

Your goal is to return the **longest possible subsequence of words** that meets these conditions.

> Hamming Distance: The number of positions at which two strings of the same length differ.

---

## Example

**Input:**

```python
words = ["bab", "dab", "cab"]
groups = [1, 2, 2]
```
### Output:
```
["bab", "dab"]
# or ["bab", "cab"]
```
## Constraints

- 1 <= n <= 1000  
- 1 <= words[i].length <= 10  
- 1 <= groups[i] <= n  
- words[i] consists of distinct lowercase English letters  

---

## Approach

- Use **Dynamic Programming (DP)**.
- Let `dp[i]` store the longest valid subsequence ending at index `i`.
- For each pair `(i, j)` where `j < i`, update `dp[i]` if:
  - `groups[i] != groups[j]`
  - `words[i]` and `words[j]` have equal length **and** Hamming distance is exactly 1.

---

## Complexity

- **Time Complexity:** O(n² * m), where `n` is the length of `words`, and `m` is the max word length (≤ 10)
- **Space Complexity:** O(n²) for storing subsequences in `dp`

---

## Tags

`Dynamic Programming` &nbsp; `Graph` &nbsp; `Subsequence` &nbsp; `String Manipulation` &nbsp; `Hamming Distance`

---

## Author

Solution prepared by **Muawiya Amir** 🚀
