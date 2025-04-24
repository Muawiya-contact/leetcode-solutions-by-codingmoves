# 🚦 LeetCode Problem 2799 - Count Complete Subarrays in an Array

![Coding Moves](https://www.youtube.com/@Coding_Moves)  
👨‍💻 By: Muawiya – AI & Mathematics Student | Founder of **@Coding_Moves**

---

## 🧠 Problem Summary

You are given an array of positive integers.  
A **subarray** is called **complete** if:

> 🔹 The number of **distinct elements** in that subarray is equal to the number of **distinct elements in the entire array**.

Your goal is to count how many such complete subarrays exist.

---

## 📥 Input

- `nums`: List of integers, where `1 ≤ nums.length ≤ 1000` and `1 ≤ nums[i] ≤ 2000`

---

## 📤 Output

- Return the total number of **complete subarrays**.

---

## 🧪 Examples

### Example 1:
```python
Input: nums = [1, 3, 1, 2, 2]
Output: 4
Explanation: The complete subarrays are:
[1,3,1,2], [1,3,1,2,2], [3,1,2], [3,1,2,2]
```
### Example 2:
```
Input: nums = [5, 5, 5, 5]
Output: 10
Explanation: Only one unique number exists, so all subarrays are complete.
```
## 🔍 Approach (Brute-force, but simple and effective)
1. Count the number of distinct elements in the full array.

2. For every possible subarray, count its distinct elements.

3. If the subarray has the same number of distinct elements, it's complete ✅

# ⏱ Time Complexity
+ O(n²) – brute force, but runs well for n ≤ 1000.

# 🔥 Author Info
## 🧑‍🎓 Muawiya

+ Dual Major: BS Artificial Intelligence @ NFC IET Multan & BS Mathematics @ VU Pakistan

+ 💡 Passion: Programming, AI, Embedded Systems, and Solving Real-World Problems

+ 🎯 Mission: Become the world's best AI Engineer & Programmer

+ 🕌 Hafiz-e-Quran | Faith + Knowledge = Power

+ 💻 Brand & Channel: @Coding_Moves

## 📹 Watch, Learn, Build!
 Check out projects, tutorials, and coding motivation at:
 👉 🎥 YouTube - [Coding Moves](https://www.youtube.com/@Coding_Moves)

# 💪 Keep Grinding!
> *"Discipline, Code, Pray, Repeat — Success Follows."
— Muawiya (Founder of Coding Moves)*

   
