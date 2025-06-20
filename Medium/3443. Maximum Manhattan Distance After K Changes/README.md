# 🚀 3443. Maximum Manhattan Distance After K Changes

## 🧠 Problem Description

You are given a string `s` consisting of the characters `'N'`, `'S'`, `'E'`, and `'W'`. These represent movements on an infinite grid:

- `'N'`: Move north (y += 1)
- `'S'`: Move south (y -= 1)
- `'E'`: Move east  (x += 1)
- `'W'`: Move west  (x -= 1)

You start at the origin `(0, 0)`. You are allowed to **change at most `k` characters** in the string to any other direction.

Find the **maximum Manhattan distance** from the origin that can be achieved at **any point during the movements**, after making at most `k` changes.

---

## 📐 Manhattan Distance

The Manhattan Distance between (x, y) and the origin (0, 0) is defined as:

```
|x| + |y|
```
---

## 🧩 Example 1:
### Input: 
```python
s = "NWSE", k = 1
```

Change s[2] from 'S' to 'N': s becomes "NWNE"

Movements:

  + N → `(0, 1)`
  
  + W → `(-1, 1)`
  
  + N → `(-1, 2)` ✅ Max Distance = 3
  
  + E → `(0, 2)`


---

## 📘 Constraints

- `1 <= s.length <= 10^5`
- `0 <= k <= s.length`
- `s` contains only `'N'`, `'S'`, `'E'`, and `'W'`

---

## ✅ Solution Strategy

- Simulate the movement **step by step**, counting how many times we go in each direction up to the current index.
- At each step, compute the current net `(x, y)` position and Manhattan Distance `MD`.
- At most `i+1` moves have been made, so the number of moves **not contributing** to the current net distance is `(i + 1 - MD)`.
- Use up to `k` changes to convert these "neutralizing" moves into moves that increase the distance:
  
 ```python
maxDistance = MD + min(2 * k, i + 1 - MD)
```

- Keep track of the maximum such distance achieved at any step.

---
🙏 Credits & Acknowledgement
Developed with ❤️ by Muawiya Amir
@Coding_Moves
Inspired by dynamic strategy optimization challenges on LeetCode.

----
