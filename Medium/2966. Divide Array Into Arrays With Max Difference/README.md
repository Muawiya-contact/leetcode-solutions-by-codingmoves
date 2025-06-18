# 2966. Divide Array Into Arrays With Max Difference

## 🧠 Problem Summary

You are given:
- An integer array `nums` of size `n` (where `n` is a multiple of 3)
- A positive integer `k`

Your task is to **divide `nums` into `n / 3` arrays of size 3**, such that:

- The **difference between any two elements** in a group is **less than or equal to `k`**

Return:
- A 2D array containing valid groups
- Or `[]` if no such division is possible

> If multiple answers exist, any of them is accepted.

---

## 🧪 Examples

### Example 1
**Input:**  
`nums = [1,3,4,8,7,9,3,5,1]`, `k = 2`  
**Output:**  
`[[1,1,3],[3,4,5],[7,8,9]]`

### Example 2
**Input:**  
`nums = [2,4,2,2,5,2]`, `k = 2`  
**Output:**  
`[]`  
**Explanation:**  
Any valid division forces 5 and 2 in same group → diff = 3 > k → invalid.

---

## ✅ Constraints

- `1 <= n <= 10^5`
- `n % 3 == 0`
- `1 <= nums[i] <= 10^5`
- `1 <= k <= 10^5`

---

## 🧩 Approach

1. **Sort** the array to group close elements.
2. Iterate through the array in **steps of 3**.
3. Check that each triplet has a **max-min difference ≤ k**.
4. If not, return `[]`. Otherwise, collect groups.

---
### ⏱ Time Complexity
  + Sorting: `O(n log n)`
  
  + Grouping: `O(n)`
  
  + Total: Efficient for up to `10^5` elements

----

### 🙌 Contributed by
Muawiya – [Coding Moves](https://www.youtube.com/@Coding_Moves)
Let's move with logic. 🚀

---
