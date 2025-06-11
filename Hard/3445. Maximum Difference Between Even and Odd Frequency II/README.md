# Maximum Difference Between Even and Odd Frequency II

## Problem

You are given a string `s` consisting of digits from `'0'` to `'4'`, and an integer `k`. Your task is to find the **maximum difference** between the frequency of two characters `freq[a] - freq[b]` in a **substring `subs`** of `s`, such that:

- `subs` has a length of **at least `k`**
- Character `a` appears with **odd frequency** in `subs`
- Character `b` appears with **even frequency** in `subs`

Return the maximum such difference. If no valid pair is found, return `-1`.

---

## Example

### Example 
### Input: 
```python
s = "12233", k = 4
````
### Output: 
```python
-1
```
---

## Constraints

- `3 <= s.length <= 3 * 10^4`
- `1 <= k <= s.length`
- `s` contains only digits from `'0'` to `'4'`
- At least one valid substring exists

---
## Solution Approach

- Iterate over all **distinct pairs** of characters `(a, b)`
- Use a **prefix count and sliding window** method to track frequencies
- Maintain a `best[]` array of minimal values for all **parity status combinations** of `(a, b)`
- Maximize the expression `(cnt_a - cnt_b) - best[required_status]` where:
  - `cnt_a` = current prefix count of `a`
  - `cnt_b` = current prefix count of `b`
  - `required_status` is derived from bitwise parity conditions
- The `getStatus` function encodes odd/even state in two bits:
  - Bit 1 = parity of `a`, Bit 0 = parity of `b`

---
### Credits
  + Problem inspired by LeetCode Problem 3445

  + Solution implemented by Muawiya

---
