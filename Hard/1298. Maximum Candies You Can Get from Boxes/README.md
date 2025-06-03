# 🎁 Maximum Candies You Can Get from Boxes

**Problem ID:** 1298  
**Difficulty:** Hard  
**Platform:** LeetCode  

---

## 🧠 Problem Summary

You are given `n` boxes, each labeled from `0` to `n-1`. Each box has:

- A **status** (`open` or `closed`)
- Some **candies** 🍬
- A list of **keys** that can open other boxes 🗝️
- A list of **contained boxes** inside it 📦

You start with a list of `initialBoxes` that you can access. Your goal is to **open as many boxes as possible** and **collect the maximum number of candies** following these rules:

1. You can open a box if it is **already open** or if you **have a key** for it.
2. When you open a box, you can:
   - Take its candies 🍬
   - Collect any keys 🗝️
   - Get access to any contained boxes 📦

You repeat this process until no more boxes can be opened.

---

## ✅ Example

### Example 1

### Input:
```python
status = [1, 0, 1, 0]
candies = [7, 5, 4, 100]
keys = [[], [], [1], []]
containedBoxes = [[1, 2], [3], [], []]
initialBoxes = [0]
```
### Output: 
```python
16
```
### Explanation:

- Start with box `0` (open): take `7` candies, get box `1` (closed) and box `2` (open).
- Open box `2`: take `4` candies, find key to box `1`.
- Open box `1`: take `5` candies, get box `3` (closed, no key).
- Can't open box `3` → done.

Total = `7 + 4 + 5 = 16`

---

## 🚀 Approach

- Use **BFS (Breadth-First Search)** with a `queue` to explore openable boxes.
- Maintain:
  - `owned_boxes`: boxes you possess.
  - `available_keys`: keys you have collected.
  - `visited`: to avoid reprocessing boxes.
- Keep opening boxes and collecting keys and new boxes until no more progress is possible.
---
### 🧪 Constraints
+ `1 <= n <= 1000`

+ `0 <= candies[i] <= 1000`

+ `status[i]` ∈ {0, 1}

+ All `keys[i]` and `containedBoxes[i]` contain unique values

+ Each box appears in `containedBoxes` at most once
--- 
