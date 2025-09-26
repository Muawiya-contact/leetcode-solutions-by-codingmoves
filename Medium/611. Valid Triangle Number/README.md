# 611. Valid Triangle Number

## 📘 Problem Statement
Given an integer array `nums`, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

A triangle is valid if the sum of any two sides is **greater** than the third side.

### Example 1:
**Input:**
```py
nums = [2,2,3,4]
```
**Output:**
```py
3
```
**Explanation:**
Valid triplets are:
- (2, 3, 4) using the first `2`
- (2, 3, 4) using the second `2`
- (2, 2, 3)

---

## 🔹 Constraints
- 1 ≤ nums.length ≤ 1000  
- 0 ≤ nums[i] ≤ 1000  

---

## 🔑 Key Insight
For a valid triangle `(a, b, c)`:
```py
a + b > c
a + c > b
b + c > a
```


### Example 2:
**Input:**
