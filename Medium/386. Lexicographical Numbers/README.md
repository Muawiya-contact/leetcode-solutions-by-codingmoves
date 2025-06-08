# 📘 386. Lexicographical Numbers

**Difficulty:** Medium  
**Tags:** DFS, Lexicographical Order, Simulation  
**Platform:** [LeetCode](https://leetcode.com/problems/lexicographical-numbers/)

---

## 🧩 Problem Statement

Given an integer `n`, return all the numbers in the range `[1, n]` sorted in **lexicographical order** (dictionary order).  
You must write an algorithm that runs in **O(n)** time and uses **O(1)** extra space (excluding output list).

---

### 📥 Input:
- An integer `n` (1 ≤ n ≤ 50,000)

### 📤 Output:
- A list of integers in lexicographical order

---

### 📘 Example 1:
### Input: 
```python
n = 13
```
### Output: 
```python
[1,10,11,12,13,2,3,4,5,6,7,8,9]
```
### 🔍 Explanation
Think of numbers as strings and sort them like words in a dictionary.
For example:
"1", "10", "11", ..., "2", "3", ..., "9"

To solve this efficiently in O(n) time:

  + Use a DFS-style traversal starting from `1`
  
  + Go deeper `(curr * 10)` if possible
  
  + Else move to the next number `(curr + 1)`
  
  + If the number ends in 9 or exceeds `n`, backtrack
---
### 🧠 Algorithm Steps
  + Start from `curr = 1`
  
  + Add `curr` to result list
  
  + If `curr * 10 <= n:` go deeper
  
  + Else if `curr + 1 <= n` and not ending in 9: go to next sibling
  
  + Else: backtrack by dividing `curr` until a valid next sibling is found

 ---
 ### ✅ Time and Space Complexity
  + Time Complexity: `O(n)`
  
  + Space Complexity: `O(1)` extra space (excluding the output list)

---
### 📚 Related Topics
  + Depth-First Search
  
  + String Sorting Simulation
  
  + Lexicographical Traversal

---  
