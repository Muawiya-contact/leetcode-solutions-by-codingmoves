# LeetCode 2894 - Divisible and Non-divisible Sums Difference

## 🧠 Problem Description

You are given two **positive integers** `n` and `m`.  
Define two values:

- `num1`: The sum of all integers in the range `[1, n]` that are **not divisible** by `m`.
- `num2`: The sum of all integers in the range `[1, n]` that **are divisible** by `m`.

**Return:** The difference `num1 - num2`.

---

## ✍️ Examples

### Example 1
### Input:
```python
n = 10, m = 3
```
### Output: 
```
19
```
### Explanation:
 + Not divisible by 3: `[1, 2, 4, 5, 7, 8, 10]` → `num1 = 37`
 + Divisible by 3: `[3, 6, 9]` → `num2 = 18`
 + Result = 37 - 18 = `19`
---
## ✅ Constraints

- `1 <= n, m <= 1000`

---

## 💡 Approach

We iterate from `1` to `n` and for each number:
- If it **is not divisible** by `m`, we add it to `num1`.
- If it **is divisible** by `m`, we add it to `num2`.

Finally, we return the difference `num1 - num2`.

This is a straightforward `O(n)` time and `O(1)` space solution using running totals.

---
## 🌟GitHub Profile Best Practices
  ✅ Add meaningful README files
  ✅ Write clean and optimized code
  ✅ Use example inputs/outputs
  ✅ Add problem tags or links if public
  ✅ Maintain consistent formatting
---
