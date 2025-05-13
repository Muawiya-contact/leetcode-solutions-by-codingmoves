# Total Characters in String After Transformations I

This project implements a solution to the LeetCode problem [3335. Total Characters in String After Transformations I](https://leetcode.com/problems/total-characters-in-string-after-transformations-i/). The goal is to determine the length of a string after performing a series of transformations.

## 🧠 Problem Description

You are given:
- A string `s` consisting of lowercase English letters.
- An integer `t`, representing the number of transformations.

### Transformation Rules:
In each transformation:
- If a character is `'z'`, it is replaced with `"ab"`.
- Otherwise, the character is replaced with the **next** character in the alphabet.  
  Example: `'a' → 'b'`, `'y' → 'z'`.

You must return the **length** of the final string after exactly `t` transformations.  
Since the result can be large, return the answer **modulo 10⁹ + 7**.

---

## 📥 Input
- `s`: a string of length up to 10⁵.
- `t`: an integer up to 10⁵.

## 📤 Output
- An integer: final length of the transformed string modulo 10⁹ + 7.

---

## ✅ Examples

### Example 1

#### Input: 
    ```
  s = "abcyy", t = 2
    ```
Output: 
  ```
    7
```
## 🚀 Optimized Solution Approach

### Strategy:
Rather than transforming the string character-by-character, which is inefficient for large inputs, we use a frequency array to track how many of each letter exist at each transformation step.

---

### Steps:
- Create a frequency array of size 26 (`a` to `z`).
- Count initial frequencies from the input string.
- For each transformation step:
  - Characters from `'a'` to `'y'` are shifted to the next character.
  - `'z'` is replaced by both `'a'` and `'b'`.
- Sum the frequencies after all transformations.

---

### ⏱️ Time & Space Complexity:
- **Time:** O(t × 26) ⇒ Efficient for large `t`
- **Space:** O(1) (only 26 elements needed)

---

## 📎 Related Topics
- String Manipulation  
- Frequency Counting  
- Modulo Arithmetic  
- Optimization Techniques

---

## 📚 License
This project is for educational purposes only and may be used or extended freely.

---

## 🙌 Acknowledgements
Problem from [LeetCode](https://leetcode.com/). Optimized approach inspired by frequency-counting strategies.

