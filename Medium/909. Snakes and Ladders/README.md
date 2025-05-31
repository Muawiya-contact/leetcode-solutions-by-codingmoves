# 🐍 Snakes and Ladders – LeetCode 909

## 🧩 Problem Description

You are given an `n x n` board representing a **Snakes and Ladders** game. The board is numbered from `1` to `n^2` in a **Boustrophedon** style (zigzag row-by-row, starting from bottom-left).

### 🎯 Objective
- Start at square `1`.
- Each move, roll a 6-sided die to choose a destination in `[curr + 1, curr + 6]`.
- If the destination has a **ladder or snake** (i.e., board cell value != -1), you **jump** to that square.
- Reach square `n^2` in the **least number of dice rolls**.

> Note: You only take **one jump per move** even if the jump leads to another snake/ladder.

---

## 🧠 Approach

This is a classic **shortest path** problem on a graph, solved using **Breadth-First Search (BFS)**:

- Each square is treated as a node.
- You roll a die (1–6) to explore edges to the next 6 positions.
- If a square has a ladder/snake, jump to its destination.
- Use a `min_rolls` array to track the minimum number of dice rolls needed to reach each square.

---
### 📦 Example
### Input:
```python
board = [
  [-1,-1,-1,-1,-1,-1],
  [-1,-1,-1,-1,-1,-1],
  [-1,-1,-1,-1,-1,-1],
  [-1,35,-1,-1,13,-1],
  [-1,-1,-1,-1,-1,-1],
  [-1,15,-1,-1,-1,-1]
]
```
### Output:
```python
4
```
---
## ✅ Characteristics of a Healthy GitHub Repo

- ✅ Well-commented and readable code  
- ✅ Includes `.md` explanation files  
- ✅ Clear problem description and example  
- ✅ Uses efficient algorithms (like BFS here)  
- ✅ Solves real-world or common coding interview problems  

---

## 📚 Topics

- Graphs (BFS)  
- Simulation  
- Arrays (2D)  
- Greedy Search  

---

## 🧠 Difficulty

**Medium**

---

## 🌐 Problem Link

[LeetCode 909 – Snakes and Ladders](https://leetcode.com/problems/snakes-and-ladders/)
---
