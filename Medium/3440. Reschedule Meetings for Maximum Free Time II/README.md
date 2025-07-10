# 📅 LeetCode 3440 — Reschedule Meetings for Maximum Free Time II

## 🔗 Problem Link
[LeetCode 3440 - Reschedule Meetings for Maximum Free Time II](https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii)

---

## 🧠 Problem Summary

You're given:
- `eventTime` — total duration of an event (from time `0` to `eventTime`)
- Two arrays `startTime` and `endTime`, where `startTime[i]` and `endTime[i]` represent the start and end times of the `i-th` **non-overlapping** meeting

🧾 **Objective**:  
You are allowed to **reschedule at most one meeting** (keep its duration and within event time), so that:
- Meetings stay non-overlapping
- You **maximize** the **longest continuous free time block** during the event

---

## 💡 Key Observations

- Meetings are already **sorted and non-overlapping**
- You can move a meeting **into a free gap** if its duration fits
- The **maximum free time** may come from:
  - Combining adjacent gaps
  - Rescheduling one meeting between two free gaps

---

## 🧪 Examples

### Example 1
### Input: 
```python
eventTime = 5, startTime = [1,3], endTime = [2,5]
```
### Output: 
```python
2
```
Reschedule [1,2] to [2,3] → Free block = [0,2] = 2

---
## 🧠 Approach (Optimized)

### 1. **Build a `gap[]` array** representing the free time between meetings

### 2. **Preprocess prefix/suffix max arrays**:
- `largestRight[i]` = max gap to the right of index `i`
- Track `largestLeft` while iterating left to right

### 3. **Try merging adjacent gaps** and simulate placing a meeting in between them if it fits

---
