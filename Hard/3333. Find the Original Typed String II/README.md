# 3333. Find the Original Typed String II

**Difficulty:** Hard  
**Tags:** Dynamic Programming, Combinatorics, String Compression

## 🧩 Problem Description

Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.

You are given a string `word`, which represents the final output displayed on Alice's screen. You are also given a positive integer `k`.

Return the **total number of possible original strings** that Alice might have intended to type, **if she was trying to type a string of size at least `k`**.

Since the answer may be very large, return it **modulo** `10⁹ + 7`.

---

## 📘 Example

### Example 1:

### Input: 
```python
word = "aabbccdd", k = 7
```
### Output: 

```python
5
```
##### Explanation: 
Possible original strings:

  + "aabbccdd"
  
  + "aabbccd"
  
  + "aabbcdd"
  
  + "aabccdd"
  
  + "abbccdd"

---
## ✅ Constraints

- `1 <= word.length <= 5 * 10⁵`
- `word` consists only of lowercase English letters
- `1 <= k <= 2000`

---

## 💡 Approach

The idea is that each group of consecutive characters like `"aaa"` in the word could have been originally typed as:
- `"a"` (long press of 1 character)
- `"aa"`
- `"aaa"`

So, for each such run of characters of length `n`, the possible original contributions to the final string can be from 1 to `n` characters.

### Steps:

1. **Group Runs**: Compress the `word` into runs of same characters.
2. **Dynamic Programming**:
    - Let `dp[i]` be the number of ways to construct an original string of length `i`.
    - For each run, update the `dp` by considering all valid contributions (from 1 to length of that run).
3. **Return the sum of `dp[length]` for all `length >= k`**

---
### 🔚 Conclusion
This problem is a beautiful mix of string compression, DP, and combinatorics.
It challenges your understanding of how to count combinations with constraints — ideal for advanced interviews and contests.

----
