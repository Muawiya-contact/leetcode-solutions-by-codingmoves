# 3362.Zero Array Transformation III

## 🧩 Problem Statement

You are given:
- An integer array `nums` of length `n`.
- A 2D array `queries`, where each `queries[i] = [li, ri]`.

Each query `[li, ri]` means:
- You can **decrease** any number in `nums[li]` to `nums[ri]` by **up to 1**.
- The decrement can be **independent** for each index in the range.

---

### 🎯 Objective

Your goal is to:
- **Convert the entire `nums` array into a Zero Array** (i.e., all elements become 0).
- You may choose to **remove some queries**.
- Find the **maximum number of queries** you can remove **while still being able to zero out the array** using the remaining queries.

If it's **impossible to make `nums` all zero**, even with all the queries, return `-1`.

---

## 📥 Input

- `nums`: List of integers (0 ≤ nums[i] ≤ 1e5)
- `queries`: List of ranges [li, ri] (0 ≤ li ≤ ri < len(nums))

---

## 📤 Output

- An integer representing:
  - The **maximum number of queries that can be removed**, OR
  - `-1` if it's not possible to make all elements in `nums` zero using all queries.

---

## 🧠 Intuition

Each index `i` in `nums` must be decremented exactly `nums[i]` times.

So:
- Count how many queries cover each index.
- If `nums[i] > coverage[i]` for any `i`, return `-1` (not enough coverage).
- Then, use a **greedy or binary search approach** to find the **maximum number of queries you can remove**, while still maintaining enough total coverage per index.

---

## ✅ Examples

### Example 1

```python
Input:
nums = [2, 0, 2]
queries = [[0, 2], [0, 2], [1, 1]]

Output:
1
```
### Explanation:
Remove query `[1, 1]`. Use the other two queries to make `nums = [0, 0, 0]`.
## 🧮 Constraints

- 1 <= nums.length <= 10^5  
- 0 <= nums[i] <= 10^5  
- 1 <= queries.length <= 10^5  
- queries[i].length == 2  
- 0 <= li <= ri < nums.length  

---

## 💡 Solution Ideas

- Use a prefix sum array to track how many times each index is covered.
- Check if `nums[i] <= coverage[i]` for all `i`.
- Apply binary search on how many queries to remove.
- Use a difference array technique for efficient range updates.

---

## 👨‍💻 Author Notes

This problem is a great test of your understanding of:

- Range updates  
- Frequency coverage  
- Greedy and search techniques in algorithmic thinking  

Perfect for preparing for coding interviews and competitive programming.
---
