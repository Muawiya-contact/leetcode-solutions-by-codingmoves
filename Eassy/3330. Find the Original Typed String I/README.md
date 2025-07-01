# 🧠 LeetCode 3330 — Find the Original Typed String I

Alice is typing a string, but she might have **pressed a key for too long** (at most once), which caused some characters to repeat. You are given the final `word` she typed and must return the total number of possible **original strings** she may have meant.

---

## 🧩 Problem Statement

> Alice tried to type a string, but she might have held a key for too long once.  
> Given a string `word` (final typed version), return the **number of different original strings** that could have resulted from reducing **at most one group** of consecutive repeating characters.

---

## 📥 Input

- A string `word` of length between 1 and 100.
- `word` consists only of lowercase English letters.

---

## 📤 Output

- An integer: total number of possible original strings.

---

## ✅ Examples

### Example 1
### Input: 
```python
word = "abbcccc"
```
### Output: 
```python
5
```

### Explanation:
  + Possible original strings:
  
  + "abbcccc" (no mistake)
  
  + "abbccc"
  
  + "abbcc"
  
  + "abbc"
  
  + "abcccc"

---

## 🧠 Approach

1. Traverse the string and **group consecutive same characters**.
2. For each group with length > 1:
   - Try reducing the length of that group (simulating a typing mistake).
   - Only **one group** can be shortened.
3. Add all resulting strings into a `set` to avoid duplicates.
4. Return the count of unique strings.

---
## 🧪 Test Cases
```python 
print(count_possible_originals("abbcccc"))  # Output: 5
print(count_possible_originals("abcd"))     # Output: 1
print(count_possible_originals("aaaa"))     # Output: 4
print(count_possible_originals("aabb"))     # Output: 3
print(count_possible_originals("a"))        # Output: 1
```
---
