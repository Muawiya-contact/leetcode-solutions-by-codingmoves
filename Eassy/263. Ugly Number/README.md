# 263. Ugly Number

**Difficulty:** Easy  
**Topics:** Math, Number Theory  

---

## Problem Statement

An **ugly number** is a positive integer whose **prime factors** only include **2, 3, and 5**.

Given an integer `n`, return **true** if `n` is an ugly number, otherwise return **false**.

---

## Examples

### Example 1
**Input:**  
```python
n = 6
```
**Output:**  
```py
True
```
**Explanation:**  
6 = 2 × 3 (only factors 2 and 3 → ugly number)

---

## Approach

1. If `n <= 0`, immediately return **false** (ugly numbers must be positive).  
2. Keep dividing `n` by 2, 3, and 5 as long as it’s divisible.  
3. After removing all factors of 2, 3, and 5:
   - If the result is **1**, then `n` is ugly.  
   - Otherwise, `n` has another prime factor → not ugly.  

---
