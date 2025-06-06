# 📄 LeetCode 2434: Using a Robot to Print the Lexicographically Smallest String

## 🧩 Problem Statement

You are given a string `s` and a robot with:

- A temporary **stack** `t` (initially empty)
- A final **output** string `p` (also initially empty)

You can repeatedly apply one of two operations:

1. **Push**: Remove the first character from `s` and push it to the top of stack `t`.
2. **Pop**: Remove the last character from `t` and append it to `p`.

Repeat these operations until both `s` and `t` are empty. Your goal is to return the **lexicographically smallest string `p`** possible.

---

## ✅ Example

### Example 1:
```text
Input: s = "bac"
Output: "abc"
```
## 💡 Approach
  + To construct the lexicographically smallest string:
  
  + Use a stack t to hold characters.
  
  + Track character frequencies with collections.Counter.
  
  + After each push, check if the top of the stack t can be popped (i.e., if it's smaller than or equal to the smallest character remaining in s).
  
  + This greedy strategy ensures we always pop the smallest possible letter available.

  ---  
