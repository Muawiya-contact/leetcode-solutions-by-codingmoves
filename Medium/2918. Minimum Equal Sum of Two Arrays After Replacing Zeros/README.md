# LeetCode Problem: 2918. Minimum Equal Sum of Two Arrays After Replacing Zeros

## Problem Statement

You are given two arrays `nums1` and `nums2` consisting of positive integers and zeros.

You must replace all the `0`s in both arrays with **strictly positive integers** such that the **sum of both arrays becomes equal**.

Your task is to return the **minimum equal sum** you can obtain, or `-1` if it's **impossible**.

---

## Example

**Input:**

```python
nums1 = [3, 2, 0, 1, 0]
nums2 = [6, 5, 0]
```
### Output
```
12
```
### Explanation:

Replace nums1’s zeros with 2 and 4, and nums2’s zero with 1. Now:

  + `nums1 = [3, 2, 2, 1, 4]` → sum = 12

  + `nums2 = [6, 5, 1]` → sum = 12

## Constraints
+ `1 <= nums1.length, nums2.length <= 10^5`

+ `0 <= nums1[i], nums2[i] <= 10^6`

## Author
Muawiya Amir
`@Coding_Moves`
    
