# 📘 LeetCode 3085 - Minimum Deletions to Make String K-Special

## 🧩 Problem Summary

You are given a string `word` and an integer `k`. A string is **k-special** if the **absolute difference** between the frequencies of **any two characters** is at most `k`.

### 🔍 Objective:
Return the **minimum number of characters** you need to delete to make the string `k-special`.

---

## 🧠 Example

### Example 1:
### Input: 
```python
word = "dabdcbdcdcd", k = 2
```
### Output: 
```python
2
```
### Explanation: 
Delete 1 'a' and 1 'd' → Frequencies become close enough

---
## 🧪 Approach

1. **Count frequency** of each character using `collections.Counter`.
2. **Try each unique frequency** as a potential target.
3. For each character:
   - If frequency < target → delete all
   - If frequency > target + k → delete extra
4. Return the **minimum deletions** required across all target frequencies.

---
### 🙏 Credits
Built with 💻 by Muawiya Amir
Follow on GitHub: @Coding_Moves

---
