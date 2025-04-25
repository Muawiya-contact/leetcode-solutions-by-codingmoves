# 🧠 LeetCode 2845: Count of Interesting Subarrays

## 💼 Problem Statement

Given a 0-indexed integer array `nums`, an integer `modulo`, and an integer `k`, you are to count the number of **interesting subarrays**.

A subarray `nums[l..r]` is considered **interesting** if:

- Let `cnt` be the number of indices `i` in the subarray such that:
nums[i] % modulo == k
- Then the subarray is interesting if:

---

## ✅ Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= modulo <= 10^9`
- `0 <= k < modulo`

---

## 🧠 Example

### Example 1:
```
Input: nums = [3, 2, 4], modulo = 2, k = 1  
Output: 3

Explanation:
Interesting subarrays:
- [3]
- [3, 2]
- [3, 2, 4]
```
### Example 2:
```
Input: nums = [3, 1, 9, 6], modulo = 3, k = 0  
Output: 2

Explanation:
Interesting subarrays:
- [3, 1, 9, 6]
- [1]
```
# 🚀 Approach
✅ Optimized Using Prefix Sum + HashMap:
+ Maintain a prefix count of how many nums[i] % modulo == k we've seen.

+ Track how many times each prefix % modulo value has occurred using a hash map.

+ For each element, compute the target prefix mod we need to form an interesting subarray:
```
target = (curr_prefix % modulo - k + modulo) % modulo
```
+ The number of times this target has appeared tells us how many valid subarrays end at the current index.

# ⏱ Complexity:
+ Time: O(n)

+ Space: O(modulo) (because prefix mod values are in [0, modulo-1])


