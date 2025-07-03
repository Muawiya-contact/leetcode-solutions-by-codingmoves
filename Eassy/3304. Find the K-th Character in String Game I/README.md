# 3304. Find the K-th Character in String Game I

## 🧩 Problem Description

Alice and Bob are playing a game. Initially, Alice has a string:
`word = "a"`

Bob repeatedly asks Alice to perform the following operation **infinitely**:

1. Change each character in `word` to its **next character** in the English alphabet (wrapping `'z'` → `'a'`).
2. Append this new string to the original `word`.

Return the **k-th character** of `word` after enough operations such that `word` has at least `k` characters.

### 🔁 Example Operations:
- `"a"` → append `"b"` → `word = "ab"`
- `"ab"` → append `"bc"` → `word = "abbc"`
- `"abbc"` → append `"bccd"` → `word = "abbcbccd"`

---

## 🧪 Examples

### Example 1:
### Input:
```python
k = 5
```
### Output: 
```python
"b"
```
---

## ✅ Constraints
- 1 ≤ k ≤ 500

---

## 🧠 Approach

We simulate the string-building process until the length of `word` reaches at least `k`. In each step:

- Convert each character to its **next letter** using `ord()` and `chr()`.
- Append the resulting string to the existing one.

---
### 🔍 Explanation of Key Functions
  - `ord(c)` – returns the Unicode number of character `c`
  
  - `chr(n)` – converts number `n` to its corresponding character
  
  - `(ord(c) - ord('a') + 1) % 26 + ord('a')` – wraps `'z'` to `'a'`

---
### 📈 Time and Space Complexity
  - **Time:** `O(k)`, since we stop building once length ≥ `k`
  
  - **Space:** `O(k)`, due to string storage

-----


    
