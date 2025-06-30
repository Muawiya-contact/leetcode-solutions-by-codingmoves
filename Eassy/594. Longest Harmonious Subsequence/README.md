# 594. Longest Harmonious Subsequence

🟢 **Difficulty**: Easy  
📚 **Topic**: HashMap, Arrays

---

## 🧠 Problem Summary

We define a harmonious array as one where the **difference between the maximum and minimum element is exactly 1**.

Given an integer array `nums`, return the **length of its longest harmonious subsequence** among all possible subsequences.

> A subsequence of an array is formed by deleting zero or more elements without changing the order of the remaining elements.

---

## 💡 Example

**Input:**  
`nums = [1,3,2,2,5,2,3,7]`  
**Output:** `5`  
**Explanation:**  
The longest harmonious subsequence is `[3,2,2,2,3]` (contains both 2s and 3s).

---

## ❌ Brute Force Approach (TLE)

Try all possible subsequences and check if `max - min == 1`.  
**Time Complexity:** `O(2^n)` — *Not suitable for n > 20*

---

## ✅ Optimized Solution (Using Counter)

We count the frequency of each number. Then for each key `k`, if `k+1` exists in the map, `count[k] + count[k+1]` is a candidate for max length.

### Python Code:
```python
from collections import Counter

class Solution:
    def findLHS(self, nums):
        count = Counter(nums)
        max_len = 0
        for num in count:
            if num + 1 in count:
                max_len = max(max_len, count[num] + count[num + 1])
        return max_len
```
---
### ⏱ Time & Space Complexity
  + Time Complexity: `O(n)` — one pass to count, one pass to check neighbors
  
  + Space Complexity: `O(n)` — for the frequency dictionary

---

