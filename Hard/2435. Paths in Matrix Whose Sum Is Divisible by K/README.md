# 🧮 LeetCode 2435 — Paths in Matrix Whose Sum Is Divisible by K

**Difficulty:** Hard  
**Topic:** Dynamic Programming  
**Status:** ✅ Solved  

---

## 📌 Problem Summary

You are given a **0-indexed `m x n` matrix `grid`** and an integer `k`.

- Start from the **top-left cell `(0,0)`**
- Reach the **bottom-right cell `(m-1, n-1)`**
- You can move **only right or down**
- Count the number of paths where the **sum of elements on the path is divisible by `k`**

Since the answer can be very large, return it **modulo `10^9 + 7`**.

---

## ✅ Key Idea

We use **Dynamic Programming with Modulo States**.

Instead of only keeping track of the number of paths, we also store  
👉 **the remainder of the path sum modulo `k`** at every cell.

---

## 🧠 DP State Definition

Let:

```py
dp[i][j][r]
```

= number of ways to reach cell `(i, j)`  
such that the **sum of the path modulo `k` equals `r`**

---

## 🔁 State Transition

From cell `(i, j)` you can come from:

- **Top:** `(i-1, j)`
- **Left:** `(i, j-1)`

For each previous remainder `prev`:

```py

new_remainder = (prev + grid[i][j]) % k
```

Update DP accordingly.

---

## 🟢 Base Case

At the start cell `(0,0)`:

```py
dp[0][0][grid[0][0] % k] = 1
```

---

## 🎯 Final Answer

Return:

```py
dp[m-1][n-1][0]
```

👉 Paths that end with sum divisible by `k`.

---

## 🧪 Example

### Input
```text
grid = [[5,2,4],
        [3,0,5],
        [0,7,2]]
k = 3

```
### Output:
```py
3
```

## ⏱️ Complexity

+ `Time: O(m × n × k)`

+ `Space: O(m × n × k)`

(Optimizable to 2 rows if needed)
