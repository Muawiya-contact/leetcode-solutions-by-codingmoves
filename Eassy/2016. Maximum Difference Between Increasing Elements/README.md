# 2016. Maximum Difference Between Increasing Elements
#### Dificulty Level : Eassy
---
## Statement:
Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), 
such that 0 <= i < j < n and nums[i] < nums[j].
> Return the maximum difference. If no such i and j exists, return -1.
---
## Example 1:
## Input:
```python
nums = [7,1,5,4]
```
## Output:
```python
4
```
# Explanation:
The maximum difference occurs with `i = 1` and `j = 2`, `nums[j] - nums[i] = 5 - 1 = 4`.
Note that with `i = 1` and `j = 0`, the difference `nums[j] - nums[i] = 7 - 1 = 6`, but `i > j`, so it is not valid.

---
## Constraints:

  + `n == nums.length`
  + `2 <= n <= 1000`
  + `1 <= nums[i] <= 109` 
----


