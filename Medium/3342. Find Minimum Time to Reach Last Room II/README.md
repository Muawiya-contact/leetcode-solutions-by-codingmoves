# 3342. Find Minimum Time to Reach Last Room II

**Difficulty**: Medium  
**Tags**: Graph, Dijkstra, Heap, Grid Traversal  

---

## 🧩 Problem Description

There is a dungeon with `n x m` rooms arranged as a grid.

You are given a 2D array `moveTime` of size `n x m`, where `moveTime[i][j]` represents the **earliest time (in seconds)** when you are allowed to enter that room.

- You start from room `(0, 0)` at time `t = 0`.
- You can move to an **adjacent** room if it shares a wall (up, down, left, right).
- Movement takes `1 second` for the first move, `2 seconds` for the second, `1` for the third, and so on (alternating between 1 and 2).

### 🏁 Goal:
Return the **minimum time** required to reach room `(n - 1, m - 1)`.

---

## ✅ Constraints

- `2 <= n == moveTime.length <= 750`
- `2 <= m == moveTime[i].length <= 750`
- `0 <= moveTime[i][j] <= 10^9`

---

## 💡 Example 1

**Input:**
```python
moveTime = [[0,4],[4,4]]
```
### Output:
```
7
```
### Explanation:

+ At t = 4, move to (1, 0) using 1 second.

+ At t = 5, move to (1, 1) using 2 seconds.

+ Reach at t = 7.

### 🛠️ Solution Approach
We use Dijkstra's algorithm with an additional dimension to track the parity (even/odd) of the number of moves taken. This lets us alternate movement durations between 1 and 2 seconds.

#### Key Steps:
+ Each cell (i, j) has 2 states:

  + Time to reach with even number of moves

  + Time to reach with odd number of moves

+ Use a min-heap to always expand the cell with the lowest time.

+ Only move into a room if current_time + move_duration >= moveTime[i][j].
---
## 📦 Applications
+ Real-time robot navigation with constraints.

+ AI movement simulation in grid-based games.

+ Resource scheduling with alternating costs.
  
