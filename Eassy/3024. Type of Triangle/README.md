# 3024. Type of Triangle

**Difficulty:** Easy  
**Topics:** Math, Arrays  
**Acceptance Rate:** 43.0%  
**Total Accepted:** 129K  
**Total Submissions:** 299.8K  

---

## 📝 Problem Statement

You are given a 0-indexed integer array `nums` of size `3` which can represent the lengths of the sides of a triangle.

A triangle is:
- **Equilateral** if all three sides are of equal length.
- **Isosceles** if exactly two sides are of equal length.
- **Scalene** if all three sides are of different lengths.

Return a **string** representing the type of triangle that can be formed:
- `"equilateral"` if all sides are equal
- `"isosceles"` if exactly two sides are equal
- `"scalene"` if all sides are different
- `"none"` if the three sides **cannot form a valid triangle**

A triangle is **valid** if and only if the sum of any two sides is **greater than** the third side.

---

## 📥 Examples

### Example 1:
### Input: 
```
nums = [3, 3, 3]
```
### Output: 
```
"equilateral"
```
### Explanation: 
All sides are equal, so it forms an equilateral triangle.
---

## ✅ Constraints

- `nums.length == 3`
- `1 <= nums[i] <= 100`

---

## 💡 Hints

- Check if the given sides form a valid triangle using the triangle inequality.
- Use `set()` to easily determine how many unique sides there are.

---
