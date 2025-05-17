# 75. Sort Colors

✅ **Solved** | 🟡 Medium | 🔢 Array | 💡 Two Pointers, Dutch National Flag Algorithm

---

## Problem Statement

Given an array `nums` with `n` objects colored red, white, or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order **red (0)**, **white (1)**, and **blue (2)**.

We will use the integers `0`, `1`, and `2` to represent the colors red, white, and blue respectively.

You must solve this problem **without using the built-in sort function**.

---

## Example 1
### Input: 
```
nums = [2,0,2,1,1,0]
```
### Output:
```
nums = [0,0,1,1,2,2]
```
## Constraints

- `n == nums.length`
- `1 <= n <= 300`
- `nums[i]` is either `0`, `1`, or `2`

--- 

## Approach

### ✅ Optimized Solution — Dutch National Flag Algorithm

This problem can be solved in **O(n)** time and **O(1)** space using the **Dutch National Flag algorithm**:

1. Initialize three pointers: `low`, `mid`, and `high`.
2. Traverse the array with `mid`, swapping elements into their correct position based on their value:
   - If `nums[mid] == 0`: Swap with `nums[low]`, increment both `low` and `mid`.
   - If `nums[mid] == 1`: Just increment `mid`.
   - If `nums[mid] == 2`: Swap with `nums[high]`, decrement `high`.
---
### Key Takeaways
  + Do not use `nums.sort()`. Focus on in-place sorting.
  
  + This is a classic example of **in-place** partitioning.
  
  + A foundational problem in mastering array manipulation and two-pointer techniques.
    
---
