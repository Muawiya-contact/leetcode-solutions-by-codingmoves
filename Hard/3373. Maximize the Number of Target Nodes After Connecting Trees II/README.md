# 3373. Maximize the Number of Target Nodes After Connecting Trees II

**Difficulty:** Hard  
**Tags:** Trees, DFS, Bit Manipulation, Graphs  

## 🧠 Problem Summary

There exist two undirected trees with `n` and `m` nodes, labeled from `[0, n - 1]` and `[0, m - 1]`, respectively.

You are given two 2D integer arrays `edges1` and `edges2` representing these trees.  
Node `u` is **target** to node `v` if the number of edges on the path from `u` to `v` is **even**.  
A node is always a target to itself.

You must connect one node from the **first tree** to one node from the **second tree** (once per node in the first tree), and for each node `i` in the first tree, determine the **maximum number of target nodes** it can have after making the connection.

Return an array `answer` of size `n`, where `answer[i]` is the maximum number of target nodes for node `i` in the first tree.

Each query is independent — the connection is reset after each one.

---

## ✅ Examples

### Example 1:
**Input:**
```python
edges1 = [[0,1],[0,2],[2,3],[2,4]]
edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
```
### Output:
```python
[8, 7, 7, 8, 8]
```
### 🔍 Key Observations
  + A node is target to another if the distance between them is even.
  
  + So we classify nodes into even and odd levels (colors) via BFS/DFS.
  
  + For any connection between two nodes `a` (from tree A) and `b` (from tree B):
  
    - If `a` is even, it can reach even-level nodes in B with even distance.
    
    - If `a` is odd, it can reach odd-level nodes in B with even distance.
    
  + The optimal number of targets for node `i` in tree A is:
    ```python
    size of colorA group to which i belongs + max(size of evenB, oddB)
    ```
 ---
  ### 📦 Input Constraints
+ `2 <= n, m <= 10^5`

+ `edges1.length == n - 1`

+ `edges2.length == m - 1`

+ Each edge consists of two distinct nodes.

+ Trees are valid (connected and acyclic)
---
### 🛠️ Complexity
 + Time: `O(n + m)`

 + Space: `O(n + m)`
---
### 🧮 Output Format
Returns a list of size n containing the maximum number of target nodes for each node in the first tree after optimal connection with the second tree.

---
### 📁 Related Topics
 + Graph Theory

 + Depth First Search (DFS)

 + Tree Coloring

 + Combinatorics
---
### 🔒 Premium Problem
This is a LeetCode premium problem and might require a subscription to access.
---
## 🧑‍💻 Author  
Solution implemented in Python by **Muawiya**

