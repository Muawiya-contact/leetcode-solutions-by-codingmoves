# 808. Soup Servings

## Problem Statement
You have two soups: **A** and **B**, each starting with `n` mL. At each turn, one of the following four serving operations is chosen **randomly**, each with probability `0.25`:

1. Pour `100 mL` from A and `0 mL` from B  
2. Pour `75 mL` from A and `25 mL` from B  
3. Pour `50 mL` from A and `50 mL` from B  
4. Pour `25 mL` from A and `75 mL` from B  

**Rules:**
- If the amount to pour is more than what remains, pour all that is left.
- The process stops immediately after **either soup runs out**.
- We want the **probability that A empties first**, plus **half the probability that both soups empty at the same time**.

---

## Examples
### Example 1:
**Input:**
```python
n = 50
```
**Output:**
```python
0.62500
```
**Explanation:**
- If operation 1 or 2 happens → A empties first (full probability).
- If operation 3 happens → both empty at the same time (half credit).
- If operation 4 happens → B empties first (no credit).

Total = `0.25 + 0.25 + 0.125 + 0 = 0.625`.

---
