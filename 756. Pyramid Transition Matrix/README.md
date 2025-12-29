# # Pyramid Transition Matrix

## Problem Description
The Pyramid Transition Matrix problem involves building a pyramid of colored blocks. Each block is represented by a letter, and each row above the bottom has one less block than the row below it. A block can be placed on top of two adjacent blocks **only if a specific allowed pattern exists**.  

- Each allowed pattern is represented as a 3-letter string: `"XYZ"`  
  - `X` = left block (bottom row)  
  - `Y` = right block (bottom row)  
  - `Z` = top block  

**Goal:** Given a bottom row and a list of allowed patterns, determine if it is possible to build the pyramid all the way to the top.

---

## Example

**Input:**

```python
bottom = "BCD"
allowed = ["BCC", "CDE", "CEA", "FFF"]
```
