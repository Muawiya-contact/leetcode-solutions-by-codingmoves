# 🪞 2081. Sum of k-Mirror Numbers

## 💡 Problem Statement

A **k-mirror number** is a positive integer that is a palindrome in both base-10 and base-`k`.

Given:
- An integer `k` (2 ≤ k ≤ 9): the base.
- An integer `n` (1 ≤ n ≤ 30): the number of such k-mirror numbers to find.

**Objective:** Return the sum of the first `n` k-mirror numbers.

---

## 🧠 Examples

### Example 1:
### Input: 
```python
k = 2, n = 5
```
### Output: 
```python
25
```
### Explanation: 
The first five 2-mirror numbers are:
  1 (1), 3 (11), 5 (101), 7 (111), 9 (1001) → Sum = 25

  ---

## 🧩 Approach

1. **Palindrome Generator (Base-10)**:
   - Construct numbers that are palindromic in decimal.
   - Separate logic for odd and even-length palindromes.

2. **Base-k Palindrome Check**:
   - Convert number to base-k and check if it is a palindrome.

3. **Two-Step Expansion**:
   - Incrementally increase the length of base-10 palindromes.
   - Check each one in base-k until `n` such numbers are found.

---
### 📈 Time & Space Complexity
  + Time Complexity: Roughly O(n log N), where N is the largest k-mirror number found.
  
  + Space Complexity: O(log N) for storing digits during base conversion.

-----
