# 🧮 LeetCode 2257 — Count Unguarded Cells in the Grid

## 🧠 Problem Summary

You are given a **grid** of size `m × n`.

- Some cells have **guards** 👮‍♂️.
- Some have **walls** 🧱.
- The rest are **empty**.

Each guard can **see in four directions** (up, down, left, right) until:
- A wall blocks the view, or  
- Another guard blocks the view, or  
- The grid edge is reached.

A cell is considered **guarded** if it is seen by at least one guard.

You must return the number of **empty cells** that are **not guarded** by any guard.

---

## 🧩 Example 1

### Input
```python
m = 4
n = 6
guards = [[0,0],[1,1],[2,3]]
walls = [[0,1],[2,2],[1,4]]
```
<img src="https://assets.leetcode.com/uploads/2022/03/10/example1drawio2.png">
### Output
```python
7
```
### Explanation:
  After simulating the guards’ vision, there are `7` cells that remain unguarded.

---
