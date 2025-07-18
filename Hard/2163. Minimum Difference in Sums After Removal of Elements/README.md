# 2163. Minimum Difference in Sums After Removal of Elements

## 🧩 Problem Statement

You are given a `0-indexed` integer array `nums` consisting of `3 * n` elements.

You are allowed to remove any subsequence of **exactly** `n` elements from `nums`. The remaining `2 * n` elements will then be split into two equal parts:

- The **first n elements**: their sum is `sumfirst`.
- The **next n elements**: their sum is `sumsecond`.

The goal is to minimize the **difference**:  
`sumfirst - sumsecond`

### Return the **minimum possible difference** after removing any `n` elements.

---

## 💡 Example

### Example 1:

```text
Input: nums = [3,1,2]
Output: -1
Explanation: n = 1. Try all 1-element removals:
- Remove 3 → [1,2] → (1) - (2) = -1
- Remove 1 → [3,2] → (3) - (2) = 1
- Remove 2 → [3,1] → (3) - (1) = 2
Minimum = -1
```
