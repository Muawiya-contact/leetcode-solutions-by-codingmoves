# Leetcode 3405: Count the Number of Arrays with K Matching Adjacent Elements

## 🚀 Problem Statement

You are given three integers `n`, `m`, and `k`. A *good array* of size `n` is defined as follows:

- Each element is between `1` and `m` (inclusive).
- Exactly `k` indices `i` (where `1 <= i < n`) satisfy `arr[i] == arr[i-1]`.

Your task is to return the number of such good arrays. Since the result may be very large, return the answer modulo `10^9 + 7`.

---

## 🧠 Approach

This is a combinatorics problem that requires:
- Choosing exactly `k` positions out of `n-1` to place equal adjacent elements.
- Assigning values from `1` to `m` such that:
  - The first element can be any value from `1` to `m`.
  - The `k` chosen positions must match the previous element.
  - The other `n - 1 - k` positions must differ from the previous one (i.e., have `m - 1` choices).

### 💡 Final Formula

```python
Total = m × (m - 1)^(n - k - 1) × C(n - 1, k)
```
---
## 🧪 Examples
### Example 1:
### Input: 
```python
n = 3, m = 2, k = 1
```
### Output: 
```python
4
```
### Explanation: 
[1,1,2], [1,2,2], [2,2,1], [2,1,1]

---
## 👨‍💻 Author
Muawiya Amir
AI Student | Full Stack Developer
GitHub: Muawiya-contact

---
