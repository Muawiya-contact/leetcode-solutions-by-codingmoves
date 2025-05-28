# Maximize the Number of Target Nodes After Connecting Trees I

**LeetCode Problem 3372 - Medium**

## 🔗 Problem Link
[LeetCode 3372 - Maximize the Number of Target Nodes After Connecting Trees I](https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/)

---

## 🧠 Problem Summary

You are given two **trees**:
- Tree 1 with `n` nodes labeled from `0` to `n - 1`
- Tree 2 with `m` nodes labeled from `0` to `m - 1`

You're allowed to connect **any one node from Tree 1 to any one node from Tree 2** using one extra edge (called a **bridge**).

A node `u` is a **target** of node `v` if there are **at most `k` edges** between them. A node is always a target to itself.

### 🎯 Task

For every node `i` in Tree 1:
- Try all possible connections (bridges) to Tree 2
- Count how many total nodes (in both trees) are reachable from `i` in ≤ `k` steps
- Return an array `answer` such that `answer[i]` is the **maximum** number of target nodes for Tree 1's node `i`.

---

## 📥 Input Format

- `edges1`: 2D array representing edges of Tree 1 (size `n-1`)
- `edges2`: 2D array representing edges of Tree 2 (size `m-1`)
- `k`: Maximum allowed path length

---

## ✅ Constraints

- `2 <= n, m <= 1000`
- `0 <= k <= 1000`
- The input graphs are always valid trees.

---

## 🧮 Example

### Input:
```python
edges1 = [[0,1],[0,2],[2,3],[2,4]]
edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
k = 2
```
### Output:
```python
[9, 7, 9, 8, 8]
```
## 🧠 Solution Approach

For each node `i` in Tree 1:

- Try connecting it to every node `j` in Tree 2
- Use **DFS** or **BFS** to count how many nodes are reachable from:
  - Node `i` in Tree 1 within ≤ `k` steps
  - Node `j` in Tree 2 within ≤ `k - 1` steps (1 step used for the bridge)
- Track the **maximum total** of reachable nodes for each `i`

### 🔧 Optimization Notes

- Use **BFS/DFS** to compute reachable nodes efficiently
- **Preprocessing** Tree 2 reachability from all nodes can improve performance

---

## 👨‍💻 Author

**Muawiya Amir**  
AI Student & Passionate Problem Solver  
- GitHub: [@MuawiyaAmir](https://github.com/MuawiyaAmir)  
- YouTube Channel: [Coding Moves](https://www.youtube.com/@Coding_Moves)

---

## 🏷️ Tags

`Graph` • `Tree` • `DFS` • `BFS` • `Distance Calculation` • `LeetCode Medium` • `Optimization`

---

## 📂 Project Structure

```
├── solution.py # Python implementation of the problem
├── README.md # This file
```
---

## 📌 Note

This project demonstrates your understanding of:

- Tree traversal  
- BFS/DFS logic  
- Optimizing across two graphs  
- Practical application of theoretical graph knowledge
---
