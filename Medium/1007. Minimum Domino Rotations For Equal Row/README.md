# 🁢 1007.Minimum Domino Rotations For Equal Row

## 🔍 Problem Statement

In a row of dominoes, each domino has two values — `tops[i]` and `bottoms[i]` — representing the numbers on the top and bottom of the *i-th* domino. You are allowed to **rotate** any domino (swap its top and bottom).

Your task is to determine the **minimum number of rotations** required to make all values in the **top row** or **bottom row** the same.

If it’s **not possible**, return `-1`.

---

## 📥 Input

- `tops`: List[int] — the values on the top halves of the dominoes.
- `bottoms`: List[int] — the values on the bottom halves of the dominoes.

**Constraints**:
- 2 <= `tops.length` <= 2 × 10⁴
- `bottoms.length` == `tops.length`
- 1 <= `tops[i]`, `bottoms[i]` <= 6

---

## ✅ Output

- An integer representing the **minimum number of rotations** needed to make all tops or all bottoms the same.
- Return `-1` if it's not possible.

---

## 💡 Example 1
### Input:
```
tops = [2,1,2,4,2,2]
bottoms = [5,2,6,2,3,2]
```

### Output:
```
2
```
**Explanation**:  
Rotating index 1 and 3 makes all top values equal to `2`.
---
## 🧠 Approach

1. Try to make all values equal to `tops[0]` or `bottoms[0]`.
2. Count the number of rotations needed in each case.
3. Return the **minimum rotations** or `-1` if neither candidate works.

---


