# 🚧 Leetcode Problem 838: Push Dominoes

## 📝 Problem Description

There are `n` dominoes in a row, and some dominoes are pushed either to the left (`'L'`) or to the right (`'R'`). The rest (`'.'`) are standing upright.

After each second:
- A domino falling to the **left** will push its **left** neighbor.
- A domino falling to the **right** will push its **right** neighbor.
- If a standing domino is pushed from **both sides** simultaneously, it stays upright.

You need to simulate and return the **final state** of all dominoes.

---

### 🔍 Example 1:

**Input:**
```
dominoes = "RR.L"
```
**Output:**
```
"RR.L"
```
**Explanation:** The dominoes do not affect each other as they are not adjacent.
---

## ✅ Constraints

- `1 <= dominoes.length <= 10^5`
- `dominoes[i]` is `'L'`, `'R'`, or `'.'`

---

## 💡 Efficient Approach (Two-Pointer Simulation)

Instead of simulating second-by-second, we analyze the dominoes **between each force** (i.e., between `'L'`, `'R'`, and `'.'` blocks) and decide the final outcome directly.

### ✔️ Time Complexity:
- **O(n)**

### ✔️ Space Complexity:
- **O(1)** (excluding output string)

---
### 💬 Author
Muawiya (aka Coding Moves)
