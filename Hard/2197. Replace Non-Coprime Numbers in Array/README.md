# Problem: Replace Non-Coprime Numbers in Array (LeetCode 2197)

## Problem Statement
You are given an array of integers `nums`. The task is to repeatedly merge adjacent **non-coprime** numbers:

1. Find two adjacent numbers that are non-coprime (i.e., their GCD > 1).
2. Replace them with their **LCM (Least Common Multiple)**.
3. Repeat until no such pairs exist.
4. Return the final modified array.

It can be proven that the final result is unique regardless of the order of merges.

---

## Key Definitions
- **Coprime numbers**: Two numbers whose GCD = 1 (e.g., 4 and 9).
- **Non-coprime numbers**: Two numbers whose GCD > 1 (e.g., 6 and 4).
- **LCM (Least Common Multiple)**: The smallest number that both numbers divide into.

---

## Example 1
**Input**:  
`nums = [6,4,3,2,7,6,2]`

**Process**:  
- (6,4) → merge → `[12,3,2,7,6,2]`  
- (12,3) → merge → `[12,2,7,6,2]`  
- (12,2) → merge → `[12,7,6,2]`  
- (6,2) → merge → `[12,7,6]`  

**Output**:  
`[12,7,6]`

---

## Example 2
**Input**:  
`nums = [2,2,1,1,3,3,3]`

**Process**:  
- (3,3) → merge → `[2,2,1,1,3,3]`  
- (3,3) → merge → `[2,2,1,1,3]`  
- (2,2) → merge → `[2,1,1,3]`  

**Output**:  
`[2,1,1,3]`

---

## Approach
We can solve this efficiently in **O(n)** using a **stack**:
1. Traverse the array from left to right.
2. Push each number onto the stack.
3. After each push, check the top two numbers:
   - If they are non-coprime, pop them and push their LCM.
   - Repeat until the top two numbers are coprime.
4. Return the final stack.

---

