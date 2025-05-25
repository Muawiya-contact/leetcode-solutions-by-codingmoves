# 🧠 LeetCode Daily Challenge - 2131. Longest Palindrome by Concatenating Two Letter Words

![LeetCode Logo](https://leetcode.com/static/images/LeetCode_logo_rvs.png)

## 🗓️ Daily Problem Progress
**Date**: Solved on Day 55  
**Status**: ✅ Accepted  
**Difficulty**: Medium  
**Username**: `Moavia_Amir`  
**Medal**: 🥇 DCC Badge Earned!  
> "Well done! Come back for tomorrow's challenge!"

---

## 🔍 Problem Description

You are given an array of strings `words`, where each element consists of **two lowercase English letters**.

Your task is to **create the longest palindrome** by selecting some elements from `words` and concatenating them in any order. Each word can be used **at most once**.
---
### 🧠 What is a Palindrome?
A **palindrome** is a string that reads the same forward and backward.

### 📝 Constraints:
- `1 <= words.length <= 10⁵`
- `words[i].length == 2`
- Each `words[i]` consists of lowercase English letters.

---

## 🧪 Examples

### ✅ Example 1:
```python
Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One palindrome is "lc" + "gg" + "cl" = "lcggcl"
```
---
### 💡 Approach
We use a greedy + hash table approach:

  + Track frequency of reversed pairs.

  + For symmetric pairs (like `"gg"`), count how many can be in the middle.

  + For non-symmetric pairs, use matched reverse pairs for palindrome construction.

---
# ⏱️ Performance

- **Runtime:** 0 ms ✅  
- **Memory:** Efficient due to fixed 26x26 frequency grid  
- **Acceptance Rate:** ~51.3%  

---

# 🏷️ Tags

`Array`, `Hash Table`, `String`, `Greedy`, `Counting`

---

# 🧠 Personal Notes

- Fun and unique challenge.
- Reinforced concepts in palindromes, pair matching, and hashing.
- Grateful for the progress on **Day 55**! 💪

---

# 📌 About This Repository

This challenge is part of my **Daily LeetCode Practice**, where I document:

- Problem statements  
- My understanding and approach  
- Clean solutions with commentary  

📺 **Follow the journey:** [@Coding_Moves on YouTube](https://www.youtube.com/@Coding_Moves)


