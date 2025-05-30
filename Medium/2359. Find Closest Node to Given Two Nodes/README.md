# LeetCode 2359 - Find Closest Node to Given Two Nodes

## 🔗 Problem Link
[LeetCode Problem 2359](https://leetcode.com/problems/find-closest-node-to-given-two-nodes/)

## 🧠 Problem Summary

You're given a directed graph represented by an array `edges`, where each node has **at most one outgoing edge**. If a node has no outgoing edge, its value is `-1`.

You are also given two nodes: `node1` and `node2`.

Your goal is to **find a common node** that:
- Is **reachable from both** `node1` and `node2`
- Has the **minimum maximum distance** from both `node1` and `node2`
- If multiple such nodes exist, return the **smallest index**
- If no such node exists, return `-1`

### Example
### Input: 
```python
edges = [2,2,3,-1], node1 = 0, node2 = 1
```
### Output: 
```python
2
```
---
### 🛠️ Approach
+ Use a modified DFS (Depth First Search) to record distances from both node1 and node2 to all other nodes.

+ Then, for every node:

  - Check if both `node1` and `node2` can reach it.
  
  - Calculate the maximum of the two distances.
  
  - Track the node that gives the minimum among these maximum values.

---
### 📈 Time and Space Complexity
  + Time Complexity: O(N), where N is the number of nodes (each node is visited at most once)
  
  + Space Complexity: O(N), to store distances from both nodes

###🧾 Notes
  + The graph may contain cycles
  
  + Each node has at most one outgoing edge, so the graph behaves like a mix of chains and loops
  
  + Efficient because we avoid revisiting nodes

### 🏁 Result
This solution efficiently finds the optimal meeting node with respect to distance from two starting nodes.
---
