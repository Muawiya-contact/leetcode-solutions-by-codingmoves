# # 1984. Minimum Difference Between Highest and Lowest of K Scores

## 🧩 Problem Overview

You are given:
- An integer array `nums` where `nums[i]` represents the score of the *i-th* student.
- An integer `k`, representing how many students you must select.

### 🎯 Goal
Pick **any `k` students** such that the **difference between the highest and lowest scores** among them is **minimum**.

Return that minimum difference.

---

## 🧠 Key Idea

To minimize the difference:
1. **Sort** the scores.
2. Check every **group of `k` consecutive scores**.
3. Compute:  
```py
difference = max_score - min_score
```
4. Return the **smallest difference** found.

Why this works:
- After sorting, close scores are adjacent.
- Picking `k` consecutive elements ensures the smallest possible range.

---


