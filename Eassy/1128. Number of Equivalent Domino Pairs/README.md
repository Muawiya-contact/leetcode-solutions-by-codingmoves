# 🁢 1128. Number of Equivalent Domino Pairs

This repository contains a solution to the LeetCode problem [1128. Number of Equivalent Domino Pairs](https://leetcode.com/problems/number-of-equivalent-domino-pairs/).

## 📘 Problem Description

Given a list of dominoes, where each domino is represented as a list of two integers `[a, b]`, two dominoes `[a, b]` and `[c, d]` are considered equivalent if:

```
(a == c and b == d) or (a == d and b == c)
```

That is, one domino can be rotated to become the other.

Return the **number of pairs** `(i, j)` such that `0 <= i < j < dominoes.length` and `dominoes[i]` is equivalent to `dominoes[j]`.

---

## 🧠 Examples

### Example 1

**Input:**
```python
dominoes = [[1,2],[2,1],[3,4],[5,6]]
```
### Output:
```
1
```
### Explanation:
Only [1,2] and [2,1] are equivalent.

## ✅ Constraints

- `1 <= dominoes.length <= 4 * 10^4`
- `dominoes[i].length == 2`
- `1 <= dominoes[i][j] <= 9`

---

## 💡 Solution Approach

- We **normalize** each domino by sorting its two values so `[2,1]` becomes `[1,2]`.
- Use a **hash map** (dictionary) to count how many times each normalized domino appears.
- For each domino that appears `n` times, the number of equivalent pairs is calculated using the formula:

```python
n * (n - 1) // 2
```
## 🙋‍♂️ Author
Muawiya – [@Coding_Moves](https://www.youtube.com/@Coding_Moves)
