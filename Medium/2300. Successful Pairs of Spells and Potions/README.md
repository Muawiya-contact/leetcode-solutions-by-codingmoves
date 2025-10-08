# 🧙‍♂️ LeetCode 2300 — Successful Pairs of Spells and Potions

## 📘 Problem Statement
You are given two positive integer arrays `spells` and `potions`, where:
- `spells[i]` represents the strength of the *i-th spell*,
- `potions[j]` represents the strength of the *j-th potion*.

You are also given an integer `success`.

A **pair (spell, potion)** is considered **successful** if:

> `spell × potion ≥ success`

Your task is to return an integer array `pairs` of length `n` where:
> `pairs[i]` = the number of potions that form a successful pair with the i-th spell.

---

## 🧩 Example 1
**Input:**
```python
spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7
```
### Output:
```py
[4, 0, 3]
```
## Explanation:

+ Spell 5: `5×[1,2,3,4,5]` → `[5,10,15,20,25]` → 4 successful

+ Spell 1: `1×[1,2,3,4,5]` → `[1,2,3,4,5]` → 0 successful

+ Spell 3: `3×[1,2,3,4,5]` → `[3,6,9,12,15]` → 3 successful

✅ Result = [4, 0, 3]

---
