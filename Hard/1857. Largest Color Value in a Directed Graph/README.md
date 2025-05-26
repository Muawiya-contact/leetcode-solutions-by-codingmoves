# 🧠 LeetCode Problem: 1857. Largest Color Value in a Directed Graph

## 🔗 Problem Link
[LeetCode 1857 - Largest Color Value in a Directed Graph](https://leetcode.com/problems/largest-color-value-in-a-directed-graph/)

---

## 📄 Problem Description

You are given a **directed graph** with `n` nodes and `m` edges. Each node has a **color**, represented as a lowercase English letter.

- `colors[i]` gives the color of node `i`.
- Each `edges[j] = [a, b]` means there is a directed edge from node `a` to node `b`.

A **valid path** is a sequence of nodes `x1 -> x2 -> ... -> xk`, such that there is an edge from `xi` to `xi+1` for all `1 ≤ i < k`.

> The **color value** of a path is the number of times the most frequent color appears on that path.

### ❓ Objective

Return the **largest color value** of any valid path in the graph. If the graph contains a **cycle**, return `-1`.

---

## 🧪 Examples

### Example 1

### Input:
```python
colors = "abaca"
edges = [[0,1],[0,2],[2,3],[3,4]]
```

### Output:
```
3
```
### Explanation:
```
The path 0 -> 2 -> 3 -> 4 has colors a -> a -> c -> a.
The most frequent color is "a", which appears 3 times.
```
## ✅ Constraints

- `n == colors.length`
- `1 <= n <= 10⁵`
- `0 <= m <= 10⁵`
- `colors[i]` is a lowercase English letter.
- `0 <= a, b < n`

---

## 💡 Approach

- **Graph Representation**: Build an adjacency list using the given edges.
- **DFS with Cycle Detection**: Use a DFS approach and a visited array with 3 states:
  - `0`: unvisited
  - `1`: visiting (used to detect cycles)
  - `2`: fully visited
- **Color Count Matrix**: For each node, keep track of a list of 26 integers (for each alphabet letter) to count color frequencies on paths.
- **Recursive DFS Logic**:
  - If a node is being visited again while still in the recursion stack → **cycle detected**.
  - Update the color count from all child nodes.
  - After processing all children, increase the count of the current node’s color.
- **Answer Tracking**: Keep the maximum color frequency across all valid paths.

---

## 🚀 Time and Space Complexity

- **Time Complexity**: `O(n + m)`
  - We visit each node and edge once during DFS.
- **Space Complexity**: `O(n * 26 + n + m)`
  - Color count matrix (`n x 26`)
  - Visited array (`n`)
  - Adjacency list for edges (`m`)

---

## 📌 Tags

- Graph  
- DFS  
- Topological Sorting  
- Cycle Detection  
- Dynamic Programming on Graphs  

---

## ✨ Related Problems

- [207. Course Schedule](https://leetcode.com/problems/course-schedule/)
- [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
- [133. Clone Graph](https://leetcode.com/problems/clone-graph/)

---

## 🙌 Acknowledgement

This solution handles both **cycle detection** and **color frequency tracking** using DFS and dynamic programming, making it efficient even for large inputs.

---

> **Author**: Solution by **Muawiya**
---
