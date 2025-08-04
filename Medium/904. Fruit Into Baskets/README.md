# 🍎 904. Fruit Into Baskets

**Difficulty**: Medium  
**Tags**: Sliding Window, Hash Table, Arrays, Two Pointers  

---

## 🧾 Problem Statement

You are visiting a farm that has a single row of fruit trees. Each tree is represented by an integer in an array `fruits`, where `fruits[i]` is the type of fruit the ith tree produces.

You want to collect as much fruit as possible under these rules:

- You only have **two baskets**.
- Each basket can only hold **one type** of fruit, but **unlimited quantity**.
- You must start at any tree and pick **exactly one fruit from every tree** while moving **to the right**.
- The fruits you pick must **fit into your baskets**.
- You must stop if a tree produces a fruit that **cannot go into your baskets**.

🔄 Return the **maximum number of fruits** you can collect this way.

---

## 🧠 Intuition

This is a variation of the **"Longest Substring with at Most 2 Distinct Characters"** problem.

We can solve this using the **Sliding Window** technique, where we maintain a window of at most **2 distinct fruit types**.

---

## ✅ Approach

- Use two pointers (`left` and `right`) to define a sliding window.
- Use a `defaultdict` to **count the types of fruits** in the current window.
- Expand the window to the right as long as there are **≤ 2 types** of fruits.
- Shrink the window from the left if there are **> 2 types**.
- Keep track of the **maximum window size** (i.e., maximum fruits collected).

---


