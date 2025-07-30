# 🧠 LeetCode 2419: Longest Subarray With Maximum Bitwise AND

## 🏷️ Problem Description

You are given an integer array `nums` of size `n`.  
Your task is to **find the length of the longest subarray** that has the **maximum possible bitwise AND**.

- A **subarray** is a **contiguous** sequence of elements.
- The **bitwise AND** of an array is the result of applying the AND operation to all its elements.

---

## 🧩 Example 1

**Input:**  
`nums = [1, 2, 3, 3, 2, 2]`  
**Output:**  
`2`  
**Explanation:**  
- The maximum bitwise AND is `3`.
- The subarray `[3, 3]` gives this AND and has length `2`.

---

## 🧩 Example 2

**Input:**  
`nums = [1, 2, 3, 4]`  
**Output:**  
`1`  
**Explanation:**  
- The maximum bitwise AND is `4`.
- Only one subarray `[4]` satisfies this condition.

---

## 🧠 Approach

### Step-by-Step Strategy:
1. Find the **maximum value** in the array. This is the **best possible AND** value any subarray can achieve.
2. Traverse the array and find the **longest consecutive sequence** of this max value.
3. Return the **length** of this sequence.

---
 
