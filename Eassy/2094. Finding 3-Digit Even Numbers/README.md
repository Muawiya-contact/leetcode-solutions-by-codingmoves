# 🚀 Leetcode Problem 2094: Finding 3-Digit Even Numbers

## 🔍 Problem Statement

You are given an integer array `digits`, where each element is a digit (0–9). The array may contain duplicates.

You must find **all unique 3-digit even numbers** that:
- Are formed by **concatenating any 3 digits** from the input array.
- **Do not start with a leading zero**.
- Are **even numbers**.
- Use digits **only as many times as they appear** in the input.

Return the list of integers in **sorted order**.

---

## 📥 Example 1

**Input:**
```python
digits = [2, 1, 3, 0]
```
### Output:
```
[102, 120, 130, 132, 210, 230, 302, 310, 312, 320]

```
## 🧠 Time Complexity

- **Time:** O(900 × 3) = O(2700), where 900 is the number of 3-digit numbers (100–999)
- **Space:** O(1), ignoring the output list, since digit count is constant-sized

---

## 📌 Constraints

- `3 <= digits.length <= 100`
- `0 <= digits[i] <= 9`

---

## 🏁 How to Run

Paste the code into a Python script or Jupyter Notebook:

```python
solution = Solution()
print(solution.findEvenNumbers([2, 1, 3, 0]))
```
## 💡 Author  
**Muawiya Amir** — AI Student & Mathematician | [@Coding_Moves](https://youtube.com/@Coding_Moves)
