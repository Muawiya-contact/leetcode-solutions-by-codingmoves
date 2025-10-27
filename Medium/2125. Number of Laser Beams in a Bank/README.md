# 🏦 2125. Number of Laser Beams in a Bank

**Level:** Medium  
**Topics:** Array, String, Simulation  

---

## 🧩 Problem Description

Anti-theft security devices are activated inside a bank.  
You are given a `0-indexed` binary string array `bank` representing the floor plan of the bank, which is an `m x n` 2D matrix.

- Each `bank[i]` represents the **i-th row**, consisting of `'0'`s and `'1'`s.  
- `'0'` → empty cell  
- `'1'` → security device  

There is **one laser beam** between any two security devices if:

1. The two devices are located on different rows `r1` and `r2`, where `r1 < r2`.  
2. For each row `i` where `r1 < i < r2`, there are **no security devices** in that row.

Each beam is independent — they don’t interfere or merge.

---

## 🧠 Example

### Example 1
```python
Input: bank = ["011001","000000","010100","001000"]
Output: 8
```
