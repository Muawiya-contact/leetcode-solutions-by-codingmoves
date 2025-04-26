# 2444. Count Subarrays With Fixed Bounds

## Problem Description

You are given an integer array `nums` and two integers `minK` and `maxK`.

A **fixed-bound subarray** of `nums` is a subarray that satisfies the following:
- The minimum value in the subarray is exactly `minK`.
- The maximum value in the subarray is exactly `maxK`.

Return the **number of fixed-bound subarrays**.

A **subarray** is a contiguous part of an array.

---

## Example 1

**Input:**
```
nums = [1, 3, 5, 2, 7, 5]
minK = 1 maxK = 5
```
**Output:**
**Explanation:**
The fixed-bound subarrays are `[1, 3, 5]` and `[1, 3, 5, 2]`.
## Constraints

- `2 <= nums.length <= 10^5`
- `1 <= nums[i], minK, maxK <= 10^6`

---

## Approach (Optimized)

- Use three pointers:
  - `min_pos`: Last index where `nums[i] == minK`
  - `max_pos`: Last index where `nums[i] == maxK`
  - `bad_pos`: Last index where `nums[i]` is outside the range `[minK, maxK]`
- For each index `i`, the number of valid subarrays ending at `i` is:
 ```
max(0, min(min_pos, max_pos) - bad_pos)
```
- Add up the counts to get the final answer.

## Notes
+ `enumerate(nums)` helps us get both index and value easily in the loop.

+ This optimized approach runs in O(n) time, which is necessary because `n` can be very large (up to 100,000).

  
