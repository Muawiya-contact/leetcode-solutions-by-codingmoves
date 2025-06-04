# 🧩 LeetCode 3403 - Find the Lexicographically Largest String From the Box I

## 📝 Problem Description

Alice is organizing a game with her `numFriends` friends. In each round of the game:

- A given string `word` is split into `numFriends` non-empty parts.
- All parts are put into a box.
- No split can be repeated from any previous round.

After all valid rounds, we must find and return the **lexicographically largest string** from the box.

### 💡 Constraints:
- `1 <= word.length <= 5000`
- `word` consists only of lowercase English letters.
- `1 <= numFriends <= word.length`

---

## 🧠 Approach

Instead of generating all valid `numFriends`-part splits (which is computationally expensive), we use an **optimized greedy trick**:

### Key Insight:

> Among all possible splits into `numFriends` non-empty parts, the longest single part that can appear is of length `len(word) - numFriends + 1`.

So, we:
1. Generate all substrings of `word` of this length.
2. Find the **lexicographically largest** among them.

This efficiently simulates what could have landed in the box without brute-forcing all possible combinations.

---
## 🧪 Examples
### Example 1:
### Input: 
```python
word = "dbca"
numFriends = 2
```
### Output: 
```python
"dbc"
```
---
## 📈 Time & Space Complexity
 + Time Complexity: `O(n)` — we check each substring of a fixed length once.

 + Space Complexity: `O(1)` — only constant extra memory is used.
--- 

## ✅ Characteristics of a Healthy GitHub Project
  + This repository (or file) includes:
  
  + Clear problem statement
  
  + Optimized and well-documented solution
  
  + Example test cases
  
  + Time and space analysis

  + Clean, readable code for interviews and GitHub portfolios
---


