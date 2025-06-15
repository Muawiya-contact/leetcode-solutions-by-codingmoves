# 🧮 LeetCode 1432 - Max Difference You Can Get From Changing an Integer

## 📌 Problem Statement

You are given an integer `num`. You can perform the following operation **two separate times**:

1. Choose a digit `x` (0 ≤ x ≤ 9).
2. Choose another digit `y` (0 ≤ y ≤ 9). `y` can be equal to `x`.
3. Replace **all** occurrences of digit `x` in `num` with digit `y`.

Let `a` and `b` be the two results from applying the operation to `num`.  
Return the **maximum possible difference** between `a` and `b`.

### ⚠️ Conditions:
- `a` and `b` must not have leading zeros.
- `a` and `b` must not be zero.

---

## 💡 Example

### Example 1:
### Input: 
```
num = 555
```
### Output: 
```
888
```

### Explanation:
  + a = 999 (replace 5 with 9)
  + b = 111 (replace 5 with 1)
  + Max Difference = 999 - 111 = 888

---
## ✅ Approach

We aim to:
- **Maximize the number** by replacing the first non-9 digit with `9`.
- **Minimize the number**:
  - If the first digit is not `1`, change it to `1`.
  - Otherwise, look for a digit (not 0 or 1) to replace with `0`, avoiding leading zeros.

---

    
