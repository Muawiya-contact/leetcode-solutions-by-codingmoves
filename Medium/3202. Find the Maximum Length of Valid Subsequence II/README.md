# 3202. Find the Maximum Length of Valid Subsequence II

## 🧠 Problem Statement

You are given:
- An integer array `nums`
- A positive integer `k`

A **subsequence** `sub` of `nums` with length `x` is called **valid** if:

```python
(sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x-2] + sub[x-1]) % k
```

Return the **length of the longest valid subsequence**.

A **subsequence** is a sequence that can be derived by deleting some or no elements from the array, without changing the order of remaining elements.

---

## 🧪 Examples

### Example 1:
**Input:**  
`nums = [1, 2, 3, 4, 5]`, `k = 2`  
**Output:** `5`  
**Explanation:**  
All consecutive pairs sum to an odd number → `(a + b) % 2 = 1` → valid.

---

### Example 2:
**Input:**  
`nums = [1, 4, 2, 3, 1, 4]`, `k = 3`  
**Output:** `4`  
**Explanation:**  
One valid subsequence is `[1, 4, 1, 4]`, where every `(a + b) % 3 = 2`.

---

## 💡 Approach

We use **Dynamic Programming** with pairwise tracking:

- Let `dp[i][mod]` represent the **length of the longest valid subsequence ending at index `i`** where all consecutive pair sums `% k == mod`.

- For each pair `(j, i)` where `j < i`:
  - Compute `(nums[j] + nums[i]) % k = mod`
  - Update:  
    `dp[i][mod] = max(dp[i][mod], dp[j][mod] + 1)`

- The final answer is the **maximum value of `dp[i][mod] + 1`**, across all `i` and `mod`.

---

