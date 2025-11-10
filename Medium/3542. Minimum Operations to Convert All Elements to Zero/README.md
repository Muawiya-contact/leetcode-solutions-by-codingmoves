# 3542. Minimum Operations to Convert All Elements to Zero

**Difficulty:** Medium  
**Topics:** Array, Greedy, Simulation  
**Companies:** 🔒 Premium  
**Hint Available**

---

## Problem Statement

You are given an array `nums` of size `n`, consisting of non-negative integers.  
Your task is to apply some (possibly zero) operations on the array so that **all elements become 0**.

In **one operation**, you can select a subarray `[i, j]` (where `0 <= i <= j < n`) and set all occurrences of the **minimum non-negative integer** in that subarray to `0`.

Return the **minimum number of operations** required to make all elements in the array `0`.

---

## Examples

### Example 1

**Input:**  
`nums = [0, 2]`

**Output:**  
`1`

**Explanation:**  
Select the subarray `[1,1]` (which is `[2]`), where the minimum non-negative integer is `2`.  
Setting all occurrences of `2` to `0` results in `[0,0]`.  
Thus, the minimum number of operations required is **1**.

---

### Example 2

**Input:**  
`nums = [3,1,2,1]`

**Output:**  
`3`

**Explanation:**
1. Select subarray `[1,3]` → `[1,2,1]`, minimum is `1`.  
   After operation: `[3,0,2,0]`
2. Select subarray `[2,2]` → `[2]`, minimum is `2`.  
   After operation: `[3,0,0,0]`
3. Select subarray `[0,0]` → `[3]`, minimum is `3`.  
   After operation: `[0,0,0,0]`

Thus, the minimum number of operations required is **3**.

---

### Example 3

**Input:**  
`nums = [1,2,1,2,1,2]`

**Output:**  
`4`

**Explanation:**
1. Select subarray `[0,5]` → `[1,2,1,2,1,2]`, minimum is `1`.  
   After operation: `[0,2,0,2,0,2]`
2. Select subarray `[1,1]` → `[2]`, minimum is `2`.  
   After operation: `[0,0,0,2,0,2]`
3. Select subarray `[3,3]` → `[2]`, minimum is `2`.  
   After operation: `[0,0,0,0,0,2]`
4. Select subarray `[5,5]` → `[2]`, minimum is `2`.  
   After operation: `[0,0,0,0,0,0]`

Thus, the minimum number of operations required is **4**.

---

## Constraints

- `1 <= n == nums.length <= 10^5`
- `0 <= nums[i] <= 10^5`

---
