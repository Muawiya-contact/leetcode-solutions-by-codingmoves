# 1751. Maximum Number of Events That Can Be Attended II

## 🧩 Problem Description

You are given an array of events where each `event = [startDay, endDay, value]`:
- The event starts on `startDay` and ends on `endDay` (inclusive).
- Attending the event gives you `value`.

You're also given an integer `k`, the maximum number of events you can attend.

### Rules:
- You can attend **at most k events**.
- You can **only attend one event at a time**.
- If one event ends on the same day another begins, you **cannot** attend both.

### 🔁 Objective:
Return the **maximum total value** you can obtain by attending at most `k` non-overlapping events.

---

## 🧠 Examples

### Example 1:

### Input: 
```python
events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
```
### Output:
```python
7
```
### Explanation: 
 + Attend events [1,2,4] and [3,4,3] → total value = 4 + 3 = 7


---

## 📚 Constraints

- `1 <= k <= events.length`
- `1 <= k * events.length <= 10^6`
- `1 <= startDay <= endDay <= 10^9`
- `1 <= value <= 10^6`

---

## 🧮 Approach

We use **Dynamic Programming + Binary Search** to solve this efficiently.

### Steps:

1. **Sort** the events by start day.
2. Use **binary search** to find the next event that can be attended (no overlap).
3. Use **memoization** (`@lru_cache`) to avoid recomputation.

At each event:
- You either **skip** it or
- **Attend** it and jump to the next non-overlapping event.

---
