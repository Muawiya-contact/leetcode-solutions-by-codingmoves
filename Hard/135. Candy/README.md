# 🍬 Candy Distribution Problem (LeetCode 135)

## 🚀 Problem Statement

There are `n` children standing in a line, each with a given `rating` value. You are to distribute candies to them under the following conditions:

1. **Each child must have at least one candy.**
2. **Children with a higher rating than their immediate neighbor must get more candies.**

Return the **minimum number of candies** needed to satisfy these conditions.

---

## 🧠 Approach

This problem can be efficiently solved using a **two-pass greedy algorithm**:

- **Pass 1 (Left → Right):** Ensure that children with higher ratings than their left neighbor get more candies.
- **Pass 2 (Right → Left):** Ensure that children with higher ratings than their right neighbor still have more candies (possibly update based on max value).

---

## ✅ Algorithm Steps

1. Initialize a `candies` array with `1` for all `n` children (minimum candies).
2. Traverse left to right:
   - If `ratings[i] > ratings[i - 1]`, then `candies[i] = candies[i - 1] + 1`.
3. Traverse right to left:
   - If `ratings[i] > ratings[i + 1]`, then `candies[i] = max(candies[i], candies[i + 1] + 1)`.
4. Sum and return all values in `candies`.

---
## 📊 Examples
### Example 1
### Input:  
```python
ratings = [1, 0, 2]
```
### Output:
```python
5
```
### Explanation: 
[2, 1, 2]
---
## ⏱️ Time & Space Complexity

| Metric | Complexity |
|--------|------------|
| Time   | O(n)       |
| Space  | O(n)       |

---

## 📌 Constraints
 + `1 <= n <= 2 * 10⁴`
 + `0 <= ratings[i] <= 2 * 10⁴`

---

## 🏷️ Tags

`Greedy` &nbsp;&nbsp; `Array` &nbsp;&nbsp; `LeetCode-135` &nbsp;&nbsp; `Interview Question`

---

## 🙋‍♂️ Author

**Muawiya** – AI Student & Mathematician  
🎓 `@Coding_Moves`  
📘 Solving problems one line at a time!
 
   
