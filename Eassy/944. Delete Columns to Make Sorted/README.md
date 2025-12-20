# 944. Delete Columns to Make Sorted

## 🧩 Problem Description

You are given an array of strings `strs`, where:
- All strings have the **same length**
- Each string represents a **row** in a grid

Your task is to **delete columns** that are **not sorted lexicographically** from top to bottom.

A column is considered **sorted** if each character is **greater than or equal to** the character above it.

Return the **number of columns** that must be deleted.

---

## 🧠 Intuition

- Treat the input as a **2D grid**
- Traverse the grid **column by column**
- For each column:
  - Compare characters from **top to bottom**
  - If any character is smaller than the one above it, the column is **not sorted**
- Count such columns

---

## ✍️ Algorithm

1. Let `rows = len(strs)`  
2. Let `cols = len(strs[0])`
3. Initialize `delete_count = 0`
4. For each column:
   - Check all rows from index `1` to `rows - 1`
   - If `strs[row][col] < strs[row-1][col]`:
     - Increment `delete_count`
     - Stop checking that column
5. Return `delete_count`

---

## 🧪 Example

### Input
```text
["cba","daf","ghi"]
```
