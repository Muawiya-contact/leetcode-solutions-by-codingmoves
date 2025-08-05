# 🧺 3477. Fruits Into Baskets II

## 🟢 Difficulty: Easy  
**Category:** Array | Greedy

---

## 🧩 Problem Statement

You are given two arrays of integers, `fruits` and `baskets`, each of length `n`, where:

- `fruits[i]` represents the quantity of the ith type of fruit.
- `baskets[j]` represents the capacity of the jth basket.

From left to right, place the fruits according to these rules:

1. Each fruit type must be placed in the **leftmost available** basket with a capacity **greater than or equal** to the quantity of that fruit.
2. Each basket can hold **only one type** of fruit.
3. If a fruit type **cannot be placed** in any basket, it remains **unplaced**.

🔚 **Return the number of fruit types that remain unplaced after all possible allocations.**

---

## ✅ Example 1

```python
Input: fruits = [4, 2, 5], baskets = [3, 5, 4]
Output: 1

Explanation:
- Fruit 4 → goes into basket 5
- Fruit 2 → goes into basket 3
- Fruit 5 → cannot go into basket 4 (too small)
→ 1 fruit type is unplaced
```
