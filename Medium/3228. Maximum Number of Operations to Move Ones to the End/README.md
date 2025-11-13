# 🧮 LeetCode 3228 — Maximum Number of Operations to Move Ones to the End

**Difficulty:** Medium  
**Topic Tags:** Greedy, String, Counting

---

## 📝 Problem Statement

You are given a **binary string** `s`.

You can perform the following operation **any number of times**:

> Choose an index `i` such that `s[i] == '1'` and `s[i + 1] == '0'`.  
> Move the character `s[i]` to the **right** until it reaches the end of the string or another `'1'`.

Your task is to return the **maximum number of operations** you can perform.

---

### Example 1
```python
Input: s = "1001101"
Output: 4
```
