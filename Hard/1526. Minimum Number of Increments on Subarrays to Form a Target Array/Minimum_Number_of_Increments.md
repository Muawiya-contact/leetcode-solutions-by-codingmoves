# 1526. Minimum Number of Increments on Subarrays to Form a Target Array

**Difficulty:** Hard  
**Topics:** Array, Greedy, Prefix Difference  

---

## 🧩 Problem Recap

You are given an integer array `target`.  
You start with an array `initial` of the same length, filled with zeros.  

In **one operation**, you can:
- Choose any **subarray** of `initial`
- Increment **each element** in that subarray by `1`.

Return the **minimum number of operations** needed to form `target`.

---

## 🧠 Key Idea

To reach the target efficiently, notice that:
- When `target[i]` **increases** compared to `target[i-1]`, we must perform **extra operations**.
- When `target[i]` **decreases** or stays the same, previous increments already covered it.

So, we only count **positive increases** between adjacent elements.

---

## 🔹 Formula

\[
\text{operations} = target[0] + \sum_{i=1}^{n-1} \max(0, target[i] - target[i-1])
\]

Explanation:
- `target[0]` → the number of increments needed to make the first element from `0` to `target[0]`.
- For each `i > 0`, add the **increase** beyond the previous value.

---

## ✅ Example 1

**Input:**  
`target = [1, 2, 3, 2, 1]`

| i | target[i] | target[i-1] | Difference | Add to result |
|---|------------|-------------|-------------|----------------|
| 0 | 1 | — | — | 1 |
| 1 | 2 | 1 | +1 | ✅ |
| 2 | 3 | 2 | +1 | ✅ |
| 3 | 2 | 3 | -1 | ❌ |
| 4 | 1 | 2 | -1 | ❌ |

**Result:**  
`1 + 1 + 1 = 3`  
✅ Output: **3**

---

## ✅ Example 2

**Input:**  
`target = [3, 1, 1, 2]`

| i | target[i] | target[i-1] | Difference | Add to result |
|---|------------|-------------|-------------|----------------|
| 0 | 3 | — | — | 3 |
| 1 | 1 | 3 | -2 | ❌ |
| 2 | 1 | 1 | 0 | ❌ |
| 3 | 2 | 1 | +1 | ✅ |

**Result:**  
`3 + 1 = 4`  
✅ Output: **4**

---

## ✅ Example 3

**Input:**  
`target = [3, 1, 5, 4, 2]`

| i | target[i] | target[i-1] | Difference | Add to result |
|---|------------|-------------|-------------|----------------|
| 0 | 3 | — | — | 3 |
| 1 | 1 | 3 | -2 | ❌ |
| 2 | 5 | 1 | +4 | ✅ |
| 3 | 4 | 5 | -1 | ❌ |
| 4 | 2 | 4 | -2 | ❌ |

**Result:**  
`3 + 4 = 7`  
✅ Output: **7**

---

## 🧮 Python Code

```python
class Solution:
    def minNumberOperations(self, target):
        res = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                res += target[i] - target[i - 1]
        return res
```

---

## 🕒 Time & Space Complexity

| Complexity | Description |
|-------------|--------------|
| ⏱ **Time:** O(n) | We traverse the array once |
| 💾 **Space:** O(1) | Constant extra space |

---

## 💡 Summary

- Count how much each element **increases** over the previous one.  
- Add those increases to the first element value.  
- This greedy approach ensures **minimum operations**.

---
