# 🧮 LeetCode 3461 — Check If Digits Are Equal in String After Operations I

### 🔗 Problem Link
> [LeetCode 3461 — Check If Digits Are Equal in String After Operations I](https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/)

---

### 📝 Problem Statement

You are given a string `s` consisting of digits.  
Perform the following operation repeatedly **until the string has exactly two digits**:

- For each pair of consecutive digits in `s`, starting from the first digit,  
  calculate a new digit as the **sum of the two digits modulo 10**.
- Replace `s` with the sequence of newly calculated digits, maintaining order.

Return `true` if the final two digits in `s` are the same, otherwise `false`.

---

### 💡 Example 1

#### Input: 
```py
s = "3902"
```
#### Output: 
```py
true
```
#### Explanation:
+ 1st operation: `(3+9)%10=2`, `(9+0)%10=9`, `(0+2)%10=2` → `"292"`
+ 2nd operation: `(2+9)%10=1`, `(9+2)%10=1` → `"11"`
+ Both digits are equal → `True`

---

### ⚙️ Constraints
- `3 <= s.length <= 100`
- `s` consists of digits only (`'0'–'9'`)

---
