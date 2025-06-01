# 🎁 Distribute Candies Among Children II

**Problem ID:** Leetcode 2929  
**Difficulty:** Medium  
**Tags:** Math, Combinatorics, Brute Force Optimization

---

## 🧠 Problem Statement

You are given two positive integers `n` and `limit`.

Return the total number of ways to distribute `n` candies among 3 children such that **no child gets more than `limit` candies**.

### ✅ Constraints:
- `1 <= n <= 10^6`
- `1 <= limit <= 10^6`

---

## 📌 Examples

### Example 1:

### Input: 
```python
n = 5
limit = 2
```
### Output: 
```python
3
```
### Explanation: 
The valid distributions are (1, 2, 2), (2, 1, 2), and (2, 2, 1).
---
## 💡 Approach

To solve this problem, we:

1. Loop over the possible number of candies `a` that the first child can receive from `0` to `min(n, limit)`.
2. For each `a`, compute the number of valid combinations `(b, c)` such that:
   - `b + c = n - a`
   - `0 <= b, c <= limit`
3. For a given `a`, the valid range for `b` is:
   + lower = `max(0, n - a - limit)`
   + upper = `min(limit, n - a)`

4. The number of valid `(b, c)` pairs is:
   + `max(0, upper - lower + 1)`

We sum up the count for each valid `a` to get the final result.
---
## ⏱️ Complexity Analysis

- **Time Complexity:** `O(min(n, limit))`
- **Space Complexity:** `O(1)`

This approach is efficient and works well for the upper constraint limits.

---

## 🧾 Characteristics of a Healthy GitHub Project

- ✅ Clear and concise README  
- 🧪 Code with time and space complexity explained  
- 📂 Well-structured repository  
- 🧠 Problem-solving intuition included  
- 🧰 Clean and reusable code  
- 🌍 Scalable for competitive programming or interviews  

---

## 📚 Learn More

- [Stars and Bars Theorem](https://en.wikipedia.org/wiki/Stars_and_bars_(combinatorics))  
- [Inclusion-Exclusion Principle](https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle)  

---

## 🙋‍♂️ Author

**Muawiya** — AI Student & Mathematician  
✨ Coding Brand: [@Coding_Moves](https://www.youtube.com/@Coding_Moves)  

> “Logic will get you from A to B. Imagination will take you everywhere.” — *Albert Einstein*
---
