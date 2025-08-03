# 🥭 2106. Maximum Fruits Harvested After at Most K Steps

## 🧩 Problem Statement

You are on an infinite x-axis and want to collect fruits.  
You're given:

- A sorted list `fruits`, where `fruits[i] = [positionᵢ, amountᵢ]`
- An integer `startPos` (your starting position)
- An integer `k` (maximum number of steps you can walk)

You can walk left or right, 1 step per unit. You can walk **at most `k` steps** in total.  
At each fruit position you reach, you **collect all fruits** there.

Your goal is to return the **maximum number of fruits** you can harvest.

---

## 📘 Examples

### Example 1
#### Input: 
```python
fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4
```
#### Output: 
```python
9
```
#### Explanation: 
Move to 6 (3 fruits), then to 8 (6 fruits), steps = 3

----
