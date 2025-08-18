# 679. 24 Game 🎮

## Problem Statement
You are given an integer array `cards` of length `4`. Each card contains a number in the range `[1, 9]`.  
Using the operators `['+', '-', '*', '/']` and parentheses `(' and ')'`, determine if it is possible to arrange the numbers into a mathematical expression that evaluates to **24**.

### Rules
- Division `/` is **real division** (not integer division).  
  Example: `4 / (1 - 2/3) = 4 / (1/3) = 12`
- All operations must be binary (no unary `-`).
- Concatenation of digits is not allowed.  
  Example: `[1,2,1,2] → "12+12"` is **invalid**.

Return **true** if possible, otherwise **false**.

---

## Examples

### Example 1
```python
Input: cards = [4,1,8,7]
Output: true
# Explanation: (8 - 4) * (7 - 1) = 24
```
