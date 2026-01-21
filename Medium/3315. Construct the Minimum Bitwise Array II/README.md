# 3315. Construct the Minimum Bitwise Array II

**Difficulty:** Medium  

**Topics:** Bit Manipulation, Array  

---

## Problem Statement

You are given an array `nums` consisting of `n` **prime integers**.  

You need to construct an array `ans` of length `n` such that, for each index `i`:

```
ans[i] OR (ans[i] + 1) == nums[i]
```

Additionally:

- Minimize each value of `ans[i]` in the resulting array.
- If no such `ans[i]` exists, set `ans[i] = -1`.

### Examples

**Example 1:**

```py
Input: nums = [2,3,5,7]
Output: [-1,1,4,3]
``
