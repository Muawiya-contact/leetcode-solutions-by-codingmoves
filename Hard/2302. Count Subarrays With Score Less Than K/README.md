# 📊 Count Subarrays With Score Less Than K

This project solves the **"Count Subarrays With Score Less Than K"** problem from LeetCode using an optimized **Sliding Window** approach.

---

## 🚀 Problem Statement

The **score** of an array is defined as:

Score = (Sum of elements) × (Length of array)

You are given:
- A positive integer array `nums`
- An integer `k`

Return the number of **non-empty subarrays** whose **score** is **strictly less than** `k`.

A **subarray** is a **contiguous** part of an array.

---

## 📚 Examples

### Example 1

```text
Input: nums = [2, 1, 4, 3, 5], k = 10
Output: 6
```
### Explanation:

The 6 valid subarrays are:

+ [2] → 2 × 1 = 2

+ [1] → 1 × 1 = 1

+ [4] → 4 × 1 = 4

+ [3] → 3 × 1 = 3

+ [5] → 5 × 1 = 5

+ [2, 1] → (2 + 1) × 2 = 6

  ## 🛠️ Approach

We use a **Sliding Window** to maintain a valid subarray:

- Initialize two pointers: `left` and `right`.
- Expand the window by moving `right` and adding `nums[right]` to `current_sum`.
- If the score exceeds or equals `k`, shrink the window from the left.
- At each step, add `(right - left + 1)` to the result.

This ensures **O(N)** time complexity, where **N** is the length of `nums`.

---

## 💻 Code

```python
class Solution(object):
    def countSubarrays(self, nums, k):
        n = len(nums)
        total = 0
        left = 0
        current_sum = 0

        for right in range(n):
            current_sum += nums[right]
            while (current_sum * (right - left + 1)) >= k:
                current_sum -= nums[left]
                left += 1
            total += (right - left + 1)

        return total
```
# 🧠 Complexity Analysis
+ Time Complexity: O(N)

+ Space Complexity: O(1) (only variables used, no extra data structures)
  
