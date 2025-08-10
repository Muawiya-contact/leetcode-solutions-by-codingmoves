# 869. Reordered Power of 2

## 📝 Problem Statement
You are given an integer `n`. You can reorder its digits in any order (including the original order), but the resulting number cannot have a leading zero.

Return `true` if and only if we can reorder the digits so that the resulting number is a **power of two**.

A power of two means numbers like:
`1, 2, 4, 8, 16, 32, 64, 128, ...`
Where each is `2^k` for some non-negative integer `k`.

---

## 📌 Examples

**Example 1:**
`Input: n = 1
Output: true
Explanation: 1 is 2^0.`

---

## 🔒 Constraints
- `1 <= n <= 10^9`

---

## 💡 Approach
1. Convert `n` into a string to easily access digits.
2. Generate **all unique permutations** of the digits using `itertools.permutations`.
3. Skip permutations with a leading zero.
4. For each valid permutation, check if the number is a **power of two**.
   - A number is a power of two if `(num & (num - 1)) == 0` and `num > 0`.
5. If any permutation satisfies the condition, return `True`; otherwise, return `False`.

---

## ⏳ Complexity
- **Time Complexity:** O(k! * k) where `k` is the number of digits (factorial due to permutations).
- **Space Complexity:** O(k!) for storing unique permutations.

---

## 💻 Python Implementation
