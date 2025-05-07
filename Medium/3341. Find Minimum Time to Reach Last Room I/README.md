# 🏰 Find Minimum Time to Reach Last Room I (LeetCode 3341)

## Problem Statement

You are in a dungeon with `n x m` rooms arranged in a grid. Each room can only be entered **after a specific minimum time**, given by a 2D array `moveTime`, where:

- `moveTime[i][j]` is the earliest time you are allowed to move into room `(i, j)`
- You begin at room `(0, 0)` at time `t = 0`
- You can move **up, down, left, or right**, and **each move takes 1 second**
- You **may need to wait** before entering a room if you're early

Your goal is to return the **minimum time** to reach the **bottom-right** room `(n-1, m-1)`.

---

## Example

### Input:
```python
moveTime = [[0,4],[4,4]]
```
### Output:
```
6
```
### Explanation:
+ At t = 4, move to (1, 0)

+ At t = 5, move to (1, 1)

+ Reach at t = 6

## Constraints

- `2 <= n <= 50`
- `2 <= m <= 50`
- `0 <= moveTime[i][j] <= 10^9`

---

## Solution Explanation

We use **Dijkstra’s algorithm (BFS with a priority queue)** because:

- Each move has a uniform cost of 1 second
- We have a constraint on when we can enter a room, so we may need to wait

### Key Ideas:
- **Min-Heap:** Use a min-heap to always process the cell with the earliest possible arrival time
- **Distance Matrix (`dist`)**: Maintain a `dist` matrix to store the minimum time to reach each room
- **Wait Time Calculation:** For each adjacent room, calculate the earliest time you can enter using:
  
```python
  time_to_enter = max(current_time, moveTime[next_row][next_col]) + 1
```
## Constraints

- `2 <= n <= 50`
- `2 <= m <= 50`
- `0 <= moveTime[i][j] <= 10^9`

---
