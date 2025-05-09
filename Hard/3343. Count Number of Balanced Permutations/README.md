# 3343. Count Number of Balanced Permutations

## Problem

You are given a string `num` consisting of digits `'0'` to `'9'`.

A permutation of `num` is called **balanced** if the sum of digits at **even indices** is equal to the sum at **odd indices**.

Return the **number of distinct balanced permutations** of the string `num`.

Since the answer may be very large, return it modulo `10⁹ + 7`.

---

## Example

### Example 1:
Input: 
```
num = "123"
```
Output:
```
2
```
### Explanation:
Permutations: "123", "132", "213", "231", "312", "321"
Balanced: "132", "231"
## Constraints

- `2 <= num.length <= 80`
- `num` consists only of digits `'0'` to `'9'`

---

## Approach

This solution uses:

- **Combinatorics** to count permutations efficiently
- **Dynamic Programming** to count valid digit groupings that sum to half the total
- **Factorials and Modular Inverses** to avoid overcounting due to repeated digits

Steps:

1. If total digit sum is odd, return 0.
2. Use `dp[sum][count]` to find how many ways to select `count` digits that sum to `sum`.
3. Multiply by factorials to count arrangements.
4. Divide by inverse factorials of each digit to correct for repetitions.

---
