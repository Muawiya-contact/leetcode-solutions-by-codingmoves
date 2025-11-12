# 🧮 2654. Minimum Number of Operations to Make All Array Elements Equal to 1

**Difficulty:** Medium  
**Status:** Solved  
**Topics:** Array, Math, GCD  

---

## 🧠 Problem Statement

You are given a 0-indexed array `nums` consisting of **positive integers**.  
You can perform the following operation on the array any number of times:

> Select an index `i` such that `0 <= i < n - 1` and replace **either** `nums[i]` or `nums[i+1]` with their **GCD (greatest common divisor)** value.

Return the **minimum number of operations** required to make **all elements** of `nums` equal to `1`.  
If it is **impossible**, return `-1`.

---

## 📘 Definition

The **GCD** of two integers is the **greatest common divisor** of those integers.

---

## 🧩 Examples

### Example 1
**Input:**  
```python
nums = [2, 6, 3, 4]
```
#### Output:
```py
4
```


### ⚙️ Constraints

+ `2 <= nums.length <= 50`

+ `1 <= nums[i] <= 10^6`

----
