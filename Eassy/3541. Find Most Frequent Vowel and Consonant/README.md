# MAT 3541 – Find Most Frequent Vowel and Consonant

## Problem Statement
Given a string `s`, find the most frequent **vowel** and the most frequent **consonant** in the string.  
Return the **sum of their frequencies**.

- **Vowels:** a, e, i, o, u  
- **Consonants:** all other English alphabets

If the string contains only vowels or only consonants, treat the missing category’s frequency as **0**.

---

## Example

### Input
```py
s = "abcdeeeiooo"
```

### Processing
- Vowel frequencies:  
  - `a = 1, e = 3, i = 1, o = 3` → max vowel = 3  
- Consonant frequencies:  
  - `b = 1, c = 1, d = 1` → max consonant = 1  

### Output
```
4
```
## Constraints
- String `s` consists of lowercase English letters.
- `1 <= len(s) <= 10^5`

---

## Approach
1. Use a frequency counter (`collections.Counter`) to count each character.  
2. Extract the maximum frequency among vowels.  
3. Extract the maximum frequency among consonants.  
4. Return their sum.  

This ensures **O(n)** time complexity and efficient performance.

---
