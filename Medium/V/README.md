# Next Greater Numerically Balanced Number

## Problem Description

An integer `x` is **numerically balanced** if for every digit `d` in the number `x`, there are exactly `d` occurrences of that digit in `x`.  

Given an integer `n`, return the **smallest numerically balanced number strictly greater than `n`.**

### Examples

**Example 1:**
### Input:
```py
n = 1
```
### Output: 
```py
22
```
### Explanation:
  + 22 is numerically balanced since the digit `2` occurs `2` times.
  + It is the smallest numerically balanced number strictly greater than `1`.

---

### Constraints
- `0 <= n <= 10^6`

---

## Approach

1. **Brute-force check:**  
   - Start checking numbers from `n + 1` upwards.
   - Convert the number to a string to count digits.
   - For each digit `d`, check if it appears exactly `d` times.
   - Return the first number that satisfies the condition.

2. **Why it works:**  
   - Since the input constraint is small (`n <= 10^6`), iterating upwards is efficient.
   - Every number is checked for the balanced condition in a simple way.

---
