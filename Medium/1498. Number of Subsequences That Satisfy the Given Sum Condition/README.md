# 🚀 LeetCode 1498 - Number of Subsequences That Satisfy the Given Sum Condition

## 🧠 Problem Summary

Given an array of integers `nums` and an integer `target`, return the number of **non-empty subsequences** such that the **sum of the minimum and maximum elements** in the subsequence is **less than or equal to** `target`.

Since the answer may be very large, return it modulo **10⁹ + 7**.

---

## 📌 Example

### Input:
```python
nums = [3, 5, 6, 7]
target = 9
```
### Output:
```python
4
```
### Explanation:
Explanation:
The valid subsequences are:

+ `[3]`

+ `[3, 5]`

+ `[3, 6]`

+ `[3, 5, 6]`
  
----
### ✅ Constraints
  + `1 <= nums.length <= 10^5`
  
  + `1 <= nums[i] <= 10^6`
  
  + `1 <= target <= 10^6`
---
### 🔍 Approach
  1.Sort the input array to simplify max/min checking.
  
  2.Use a two-pointer approach:
    - Move `left` from the start.
    - Move `right` from the end.
  
  3.If `nums[left] + nums[right] <= target`, all subsequences between them are valid.
  
  4.Use powers of 2 to count all valid subsequences:
    - Number of `subsequences = 2^(right - left)`
  
  5.Use modulo 10^9 + 7 to avoid overflow.
  
---
## 🙌 Contributing
Feel free to fork this repo, create a branch, and submit a PR if you’d like to improve the explanation or approach!

---

