# 3480. Maximize Subarrays After Removing One Conflicting Pair

## Problem Description

You are given an integer `n` which represents an array `nums` containing the numbers from `1` to `n` in order. Additionally, you are given a 2D array `conflictingPairs`, where `conflictingPairs[i] = [a, b]` indicates that `a` and `b` form a conflicting pair.

Your task is to:
1. Remove exactly one element from `conflictingPairs`.
2. After removal, count the number of non-empty subarrays of `nums` which do not contain both `a` and `b` for any remaining conflicting pair `[a, b]`.
3. Return the maximum number of such subarrays possible after removing exactly one conflicting pair.

### Examples

#### Example 1:
**Input:**
```python
n = 4, conflictingPairs = [[2,3],[1,4]]
```
## Output:
```python
9
```
---
## Constraints
  + 2 <= n <= 10^5
  
  + 1 <= conflictingPairs.length <= 2 * n
  
  + conflictingPairs[i].length == 2
  
  + 1 <= conflictingPairs[i][j] <= n
  
  + conflictingPairs[i][0] != conflictingPairs[i][1]

---
