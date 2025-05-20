# 3355.Zero Array Transformation I

This project implements an efficient solution to the **Zero Array Transformation I** problem, a medium-level challenge that involves range-based operations on an array.

## 📘 Problem Statement

You are given:
- An integer array `nums` of length `n`.
- A list of `queries`, where each `query[i] = [li, ri]`.

For each query:
- You can select **any subset of indices** within the range `[li, ri]`.
- Decrease the values at those selected indices by 1.

Your goal is to return `True` if it's possible to turn `nums` into an array of all zeros after applying all the queries in order. Otherwise, return `False`.

---

## ✅ Example

### Input:
```python
nums = [1, 0, 1]
queries = [[0, 2]]
```
### Output:
```
True
```
### Explanation:
Pick indices 0 and 2 in the query, subtract 1 → [0, 0, 0].
---
## 💡 Why This Works

- `diff` helps in tracking how many times each index is affected by all queries.
- Instead of updating each index in every query (which is slow), we update the **boundaries** and later apply a **running total (`cnt`)**.
- At the end, if any `nums[i] > cnt`, it means we **can't decrement it enough** → return `False`.

---

## 📈 Time and Space Complexity

- **Time Complexity**: `O(n + q)` where `n = len(nums)` and `q = len(queries)`
- **Space Complexity**: `O(n)` for the difference array

---

## 📂 Files

- `solution.py` – contains the main implementation
- `README.md` – documentation of the problem and solution

---

## 🧠 Useful Concepts

- Difference array (prefix sum optimization)
- Range query optimization
- Greedy strategy for decrement tracking

---

## ✅ Characteristics of a Healthy GitHub Project

- [x] Clear problem description  
- [x] Optimized solution  
- [x] Proper file structure  
- [x] README with examples, explanation, and complexity analysis  

---

## 📬 Contact

Made with 💡 by **Muawiya** – AI Student, Mathematician, and Programmer  
Stay connected: [@Coding_Moves](https://www.youtube.com/@Coding_Moves)
---
