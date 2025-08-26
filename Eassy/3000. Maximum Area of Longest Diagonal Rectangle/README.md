# 🟦 3000. Maximum Area of Longest Diagonal Rectangle

## 📘 Problem Statement
You are given a **2D 0-indexed integer array `dimensions`**.  

- For all indices `i`, `dimensions[i][0]` represents the **length** and `dimensions[i][1]` represents the **width** of the rectangle `i`.  
- The **diagonal** of a rectangle is given by:  

\[
\text{diagonal} = \sqrt{(\text{length}^2 + \text{width}^2)}
\]

Return the **area of the rectangle** having the **longest diagonal**.  
If multiple rectangles have the same longest diagonal, return the **maximum area** among them.  

---

## 📝 Example 1
**Input:**
```python
dimensions = [[9,3],[8,6]]
```
