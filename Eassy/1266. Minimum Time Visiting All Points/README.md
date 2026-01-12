# 1266. Minimum Time Visiting All Points

## 🧠 Problem Overview

You are given a list of points on a **2D plane**.  
Each point is represented as `[x, y]`.

Your task is to calculate the **minimum time (in seconds)** required to visit **all points in the given order**.

---

## ⏱ Movement Rules

In **1 second**, you can:
- Move **up or down** by 1 unit  
- Move **left or right** by 1 unit  
- Move **diagonally** (1 unit in x and 1 unit in y at the same time)

⚠️ You must visit the points **in order**, but you may pass through other points without counting them as visits.

---

## 💡 Key Insight

To move from one point `(x1, y1)` to `(x2, y2)`:

```
dx = |x2 - x1|
dy = |y2 - y1|
```
### ✅ Minimum time needed:
max(dx, dy)


### Why?
- Diagonal moves reduce both `x` and `y` together
- Use diagonal moves as much as possible
- The larger difference decides the total time

---

## 📌 Example 1

**Input:**

```py
points = [[1,1],[3,4],[-1,0]]
```

### Calculation:
- From (1,1) → (3,4): `max(2, 3) = 3`
- From (3,4) → (-1,0): `max(4, 4) = 4`

**Total Time:**  

```
3 + 4 = 7 seconds
```

---
