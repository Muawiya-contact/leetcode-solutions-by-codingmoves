# 🧮 Problem: Find X-Sum of All K-Long Subarrays I

## 📘 Description
You are given:
- An array `nums` of integers  
- Two integers `k` and `x`

You must find the **x-sum** for each subarray of length `k`.

---

## 🧠 What is an X-Sum?

To calculate the **x-sum** of any array:

1. Count how many times each number appears.
2. Keep only the **x most frequent numbers**.  
   - If two numbers have the same frequency → choose the **bigger number** first.
3. Remove all other numbers.
4. Add up all remaining numbers.  
   → That sum is the **x-sum**.

---

## ⚙️ What the program should do
For every subarray of length `k` in `nums`, calculate its x-sum.  
Return all those results in a list.

---

## 🧩 Example

### Example 1
```python
nums = [1,1,2,2,3,4,2,3]
k = 6
x = 2
```
#### ✅ Output:
  `[6, 10, 12]`

  ---
