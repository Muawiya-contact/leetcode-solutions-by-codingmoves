# Total Characters in String After Transformations II

## Problem Statement

You are given:
- A string `s` consisting of lowercase English letters.
- An integer `t` representing the number of transformations to perform.
- An array `nums` of size 26 where `nums[i]` indicates how many new consecutive characters character `i + 'a'` should transform into.

### Transformation Rules:
In **each transformation**:
- For every character `c` in the string:
  - Replace `c` with the next `nums[c - 'a']` consecutive characters in the alphabet.
  - Wrap around after `'z'` to `'a'`.

### Goal:
After `t` transformations, return the **length** of the final string modulo `10⁹ + 7`.

---

## Example

### Input:
```
s = "abcyy"
t = 2
nums = [1,1,1,...,1,2] #(size 26)
```

### Transformation Steps:

**First Transformation:**
- `'a' → 'b'`
- `'b' → 'c'`
- `'c' → 'd'`
- `'y' → 'z'`
- `'y' → 'z'`

Result: `"bcdzz"`

**Second Transformation:**
- `'b' → 'c'`
- `'c' → 'd'`
- `'d' → 'e'`
- `'z' → 'ab'`
- `'z' → 'ab'`

Result: `"cdeabab"`

### Output:
```
7
```

---

## Constraints
- `1 <= s.length <= 10^5`
- `1 <= t <= 10^9`
- `1 <= nums[i] <= 25`

---

## Optimized Approach: Matrix Exponentiation

Because `t` can be as large as **1 billion**, direct simulation is not feasible. We use **matrix exponentiation** to compute the final result efficiently.

### Core Idea:

Let’s treat the transformation process as a **linear operation on character counts**.  
We represent character transitions using a 26×26 matrix `T`, where:
- `T[i][j]` tells how many times character `j` will appear if we transform character `i` once.

Then we compute:

```
final_counts = initial_counts × (T^t)
```

Finally, we sum the values in `final_counts`.

---

## Visual Diagram (Markdown Style)

```text
Suppose: nums['a'] = 3, so 'a' → 'b', 'c', 'd'

Matrix row for 'a':
T[0][1] = 1   # 'b'
T[0][2] = 1   # 'c'
T[0][3] = 1   # 'd'
All other T[0][j] = 0

Initial Frequency Vector:
[ freq['a'], freq['b'], ..., freq['z'] ] → 1 × 26 row matrix

Power Matrix T^t:
  (computes cumulative effect of t transformations)

Final Frequency = Initial × (T^t)

Answer = sum(final frequency vector)
```
## Time Complexity

- **Matrix Exponentiation**: `O(log t × 26³)`
- **Final Multiplication**: `O(26²)`
- ✅ Very efficient even for `t = 10⁹`.

---

## Summary

✅ Tracks only frequencies  
✅ Uses matrix exponentiation for large `t`  
✅ Final result computed in logarithmic time  
✅ No need to store large strings  
✅ Clean and scalable

