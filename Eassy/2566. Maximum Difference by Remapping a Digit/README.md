# LeetCode Problem 2566 - Maximum Difference by Remapping a Digit

## 🧠 Problem Summary

You are given an integer `num`. Bob wants to remap exactly one digit (0–9) to another digit (also 0–9) in the number. This remapping is applied to **all** occurrences of that digit.

Bob can perform two separate remappings:
- One to maximize the number
- One to minimize the number

Return the **difference between the maximum and minimum number** that can be formed after such remappings.

**Note:**
- Leading zeroes are allowed in the final number.
- Bob may remap a digit to itself (no change).

---

## 💡 Examples

### Example 1:
**Input:**  
`num = 11891`

**Process:**
- Max: Replace all `1` with `9` → `99899`
- Min: Replace all `1` with `0` → `890`

**Output:**  
`99899 - 890 = 99009`

### Example 2:
**Input:**  
`num = 90`

**Process:**
- Max: Replace `0` with `9` → `99`
- Min: Replace `9` with `0` → `0`

**Output:**  
`99 - 0 = 99`

---

## ✅ Constraints

- `1 <= num <= 10^8`

---
### 🧠 Key Takeaways
  + You only remap one digit per transformation, but it affects all occurrences of that digit.
  
  + The trick is finding the best digit to replace for both maximum and minimum results.
  
  + Leading zeroes in the result are allowed, which simplifies the logic.


---
## 🧑‍💻 Author
Muawiya – @Coding_Moves
Striving to become a Professional Machine Learning Engineer and Kaggle Grandmaster.
Follow my journey on GitHub, LeetCode, and Kaggle.

---
