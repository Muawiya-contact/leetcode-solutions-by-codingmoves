# 3068. Find the Maximum Sum of Node Values

## Problem Statement

You are given an undirected tree with `n` nodes numbered from `0` to `n - 1`.  
Each node has a non-negative value, provided in the `nums` array.  
You are also given a positive integer `k`, and an array of `edges` describing the connections in the tree.

You can perform the following operation any number of times (even zero):
- Choose any edge `[u, v]`, and apply:  
  `nums[u] = nums[u] ^ k`  
  `nums[v] = nums[v] ^ k`  

Your task is to find the **maximum sum of all node values** that can be achieved after performing these operations any number of times.

## Example

### Example 1
### Input: 
```python
nums = [1, 2, 1]
 k = 3
 edges = [[0,1],[0,2]]
```
### Output: 
```
6
```
### Explanation: 
Apply the `XOR` operation on `edge [0, 2]` once:
`nums` becomes `[2, 2, 2]` → `sum = 6`
## Constraints

- 2 <= n == nums.length <= 20,000  
- 1 <= k <= 10⁹  
- 0 <= nums[i] <= 10⁹  
- `edges.length == n - 1`  
- Edges form a valid tree

---

## Intuition

- Applying XOR to both nodes of an edge ensures the total number of XORed nodes is **always even**.
- This means we can choose to XOR values of any **even number of nodes**.
- Goal: Select a subset of nodes (even-sized) whose XOR with `k` gives a better total sum.

---

## Approach

Use dynamic programming with two states:
- `dp[0]`: Max sum with even number of XORs applied
- `dp[1]`: Max sum with odd number of XORs applied

Iterate through each node value and decide:
- Keep the value unchanged
- XOR it with `k`

Update the `dp` values accordingly.

---
## Time and Space Complexity
  + Time Complexity: O(n) — one pass through all nodes

  + Space Complexity: O(1) — only constant space used

 ---   

