# 🧮 Problem: 3354. Make Array Elements Equal to Zero

## 📝 Description
You are given an integer array `nums`.

You must:
1. Start from an index where `nums[curr] == 0`.
2. Choose a direction — **left (-1)** or **right (+1)**.
3. Then repeatedly:
   - If `curr` is **out of range**, the process stops.
   - If `nums[curr] == 0`, move one step in the same direction.
   - If `nums[curr] > 0`, subtract 1 from it, **reverse direction**, and move one step.

A start position and direction are **valid** if all elements become `0` by the end.

Return the number of possible valid selections.

---

## 🧩 Example

### Example 1
**Input:**
```python
nums = [1, 0, 2, 0, 3]
```
