# 🧩 LeetCode 11 — Container With Most Water

## 📘 Problem Statement
You are given an integer array `height` of length `n`.  
There are `n` vertical lines drawn such that the two endpoints of the `i-th` line are:
`(i, 0) and (i, height[i])`.
Find **two lines** that together with the x-axis form a **container**, such that the container contains the **most water**.

Return the **maximum amount of water** a container can store.  
Note that you may not slant the container.

---

## 🔢 Example 1
**Input:**
```python
height = [1,8,6,2,5,4,8,3,7]
```
**Output:**
```py
49

```
### Explanation:

+ The maximum area is formed between indices 1 (height = 8) and 8 (height = 7)

+ Width = 8 - 1 = 7

+ Height = min(8, 7) = 7

+ Area = 7 × 7 = 49

---

## 🧮 Formula
```py
Area = (right - left) * min(height[left], height[right])

```
# # 🚀 Optimized Two-Pointer Approach
### Intuition

+ Start with two pointers — left at the beginning, right at the end.

+ Calculate the area between them.

+ Move the pointer that has the smaller height inward to try to find a taller line.

+ Repeat until both pointers meet.

---
## ⏱️ Complexity

+ Time: `O(n)`

+ Space: `O(1)`

---
## 🎯 Key Insight

> The smaller height always limits the container’s water.
> Therefore, move the pointer with the smaller height inward to maximize area.
---
## ✨ Author

**Muawiya** — AI & Mathematics Student, 
LeetCode Practice Series 🚀
