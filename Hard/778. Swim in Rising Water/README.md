# 🏊‍♂️ LeetCode 778 — Swim in Rising Water

**Difficulty:** Hard  
**Topics:** Graphs, Priority Queue, Binary Search, BFS, Union-Find  

---

## 📖 Problem Statement

You are given an `n x n` grid of integers where each cell `grid[i][j]` represents the **elevation** at that point.

It starts raining, and the **water level rises over time**.  
At time `t`, the water level equals `t`, and you can swim between two **4-directionally adjacent** cells if their elevations are **both ≤ t**.

Your task is to return the **minimum time `t`** such that you can reach the **bottom-right corner** `(n-1, n-1)` starting from the **top-left corner** `(0, 0)`.

---

## 🧩 Example 1

```python
Input: grid = [[0,2],
               [1,3]]

Output: 3
```
### Explanation:

+ At `t = 0`, only `(0,0)` is reachable.

+ At `t = 1` or `t = 2`, you still can’t reach `(1,1)`.

+ At `t = 3`, all cells are flooded enough — path available ✅

So, the minimum time required is `3`.


---
## ⚙️ Constraints
  
  + `1 <= n <= 50`
  
  + `0 <= grid[i][j] < n²`
  
  + All values are unique
