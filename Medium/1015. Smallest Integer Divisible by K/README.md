# 🧮 LeetCode 1015 — Smallest Integer Divisible by K

Given a positive integer **K**, the task is to find the **length of the smallest positive integer** that:

- is divisible by **K**
- contains **only digit '1'**  
  (examples: `1`, `11`, `111`, `1111`, ...)

If no such number exists, return **-1**.

---

## 📌 Key Insight

A number made up only of digit `1` is always:

- **odd**  
- **never ends with 0 or 5**

So:

- If `K % 2 == 0` → ❌ impossible  
- If `K % 5 == 0` → ❌ impossible  

Because such numbers cannot divide evenly into a number that requires last digit `0`, `2`, `4`, `5`, `6`, or `8`.

---

## 🚫 Why Not Build the Actual Number?

A number like:

```
1111111111111111111
```

becomes extremely large and cannot fit in integers.

So instead, we **simulate** the number using **remainders**.

---

## ✅ Algorithm (Using Remainder Logic)

We generate the numbers:

```
1       -> remainder = 1 % k
11      -> remainder = (1*10 + 1) % k
111     -> remainder = ((1*10+1)*10 + 1) % k
...
```

General recurrence:

```
remainder = (remainder * 10 + 1) % k
```

Repeat until:

- remainder becomes **0** → number is divisible
- or we run more than **k** steps → cycle detected → ❌ impossible

### 🧠 Why max k steps?
There are only `k` possible remainders: `0, 1, 2, ..., k-1`.

If a remainder repeats, we are in a **cycle**, and will never reach 0.  
This is guaranteed by the **Pigeonhole Principle**.

---

## ✔️ Time & Space Complexity

| Item | Value |
|------|--------|
| Time | **O(k)** |
| Space | **O(1)** |
| Safe for large K | ✔️ Yes |

---

## 🧪 Example Walkthrough

### Input:
```
k = 3
```

Iteration remainders:

| Step | Number | Remainder |
|------|---------|-----------|
| 1 | 1 | 1 |
| 2 | 11 | 2 |
| 3 | 111 | 0 |

✔ Output: **3**

---

## 📦 Summary

This problem highlights a common trick in number theory and modular arithmetic:

> **Use remainder simulation instead of constructing huge numbers.**

It avoids overflow, prevents excessive memory use, and solves the problem efficiently.

---


