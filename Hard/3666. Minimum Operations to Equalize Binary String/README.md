# Problem: Minimum Operations to Equalize Binary String

**Difficulty:** Hard

---

## Problem Statement

You are given a **binary string** `s` and an integer `k`.  

- In one operation, you must choose **exactly `k` different indices** and flip each `'0' → '1'` and `'1' → '0'`.  
- Your goal is to make **all characters in the string `'1'`** using the **minimum number of operations**.  
- If it is **impossible**, return `-1`.

---

## Examples

1. **Input:** `s = "110"`, `k = 1`  
   **Output:** `1`  
   Explanation: Flip the single `'0'` to `'1'`.

2. **Input:** `s = "0101"`, `k = 3`  
   **Output:** `2`  
   Explanation: 
   - Operation 1: Flip indices `[0,1,3]` → `"1000"`  
   - Operation 2: Flip indices `[1,2,3]` → `"1111"`

3. **Input:** `s = "101"`, `k = 2`  
   **Output:** `-1`  
   Explanation: Cannot flip exactly 2 positions to make all `'1'`.

---

## Approach

We use a **BFS (Breadth-First Search) on the number of zeros**, not on the string itself:

1. Count the number of zeros `cnt0` in the string.  
2. Maintain **two `SortedSet`s** for numbers by **even/odd parity**, because after each flip, the number of zeros changes by **an even number**.  
3. Start BFS from `cnt0`. Each BFS level = 1 operation.  
4. For each state (current number of zeros `cur`):  
   - If `cur == 0`, return the number of operations.  
   - Compute the **range of possible zero counts** after one flip:  
     ```python
     l = cur + k - 2 * min(cur, k)
     r = cur + k - 2 * max(k - n + cur, 0)
     ```
   - Add all new states in the range `[l, r]` to the queue, skipping already visited states.  
5. If BFS ends and we never reach 0 zeros, return `-1`.

---

