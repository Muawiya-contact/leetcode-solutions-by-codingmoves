# 🟢 LeetCode 812: Largest Triangle Area

## 📌 Problem Statement
You are given an array of points on the X-Y plane where `points[i] = [xi, yi]`.  
Return the area of the **largest triangle** that can be formed by any three different points.  

Answers within `1e-5` of the actual answer will be accepted.

---

## 🔹 Examples

**Example 1:**
```py
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000
Explanation: The largest triangle is formed by points (0,0), (0,2), (2,0).
```
## 💡 Approach
1. A triangle can be formed using **any 3 points**.  
2. The **area of a triangle** given points `A(x1, y1), B(x2, y2), C(x3, y3)` can be calculated using the **cross product formula**:

   \[
   \text{Area} = \frac{1}{2} \cdot |(x2-x1)(y3-y1) - (x3-x1)(y2-y1)|
   \]

3. Iterate through **all combinations of 3 points**.  
4. Keep track of the **maximum area found**.  
5. Return the largest area.

---
## ⚙️ Constraints
- `3 <= points.length <= 50`  
- `-50 <= xi, yi <= 50`  
- All points are unique.  
---
