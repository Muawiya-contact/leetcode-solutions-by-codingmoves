# 🧮 LeetCode 1578 — Minimum Time to Make Rope Colorful

## 📝 Problem
You are given:
- A string `colors`, where each character represents a balloon’s color.
- An integer array `neededTime`, where `neededTime[i]` is the time to remove the `i`-th balloon.

We must make the rope **colorful** — meaning **no two consecutive balloons have the same color** — by removing some balloons.  
Return the **minimum total time** required to achieve this.

---

## 🧠 Intuition
When two or more consecutive balloons have the same color:
- We must keep **only one** of them.
- To minimize total removal time, we **keep the one with the highest removal time** and remove the rest.

So for every **group of consecutive same-colored balloons**:
- `cost = sum(neededTime of group) - max(neededTime of group)`

We can compute this efficiently in a **single pass**.

---
## 🧩 Example Walkthrough
**Input:**  
`colors = "aaabbbabbbb"`  
`neededTime = [3,5,10,7,5,3,5,5,4,8,1]`

**Groups:**  
- `"aaa"` → remove 3 + 5 = 8  
- `"bbb"` → remove 7 + 5 = 12  
- `"a"` → no removal  
- `"bbbb"` → remove 5 + 4 + 1 = 10  

✅ **Total = 8 + 12 + 10 = 30**

⏱️ **Time Complexity**  
O(n) — single pass through all balloons.

💾 **Space Complexity**  
O(1) — constant extra space.

---
