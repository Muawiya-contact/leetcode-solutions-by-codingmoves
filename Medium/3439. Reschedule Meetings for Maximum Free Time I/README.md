# 3439. Reschedule Meetings for Maximum Free Time I

**Difficulty:** Medium  
**Tags:** Sliding Window, Greedy, Arrays

## 🧩 Problem Description

You are given:
- An integer `eventTime` — total duration of an event (from `t = 0` to `t = eventTime`).
- Two integer arrays `startTime` and `endTime` of length `n`, where the `i-th` meeting takes place during `[startTime[i], endTime[i]]`.

Meetings are **non-overlapping and sorted**:  
`endTime[i] <= startTime[i + 1]`

You can **reschedule at most `k` meetings**, keeping:
- Their **duration unchanged**
- Their **relative order unchanged**
- Meetings **inside the eventTime**

The goal is to **maximize the longest continuous free time** during the event.

---

## 💡 Example 1

**Input:**
```python
eventTime = 5
k = 1
startTime = [1, 3]
endTime = [2, 5]
```

**Output:** `2`

**Explanation:**  
Move [1, 2] → [2, 3]. This leaves a free slot of [0, 2].

---
## ❗ Constraints

- `1 <= eventTime <= 10^9`
- `2 <= n <= 10^5`
- `1 <= k <= n`
- `0 <= startTime[i] < endTime[i] <= eventTime`
- `endTime[i] <= startTime[i + 1]` for all valid `i`

---

## 🧠 Approach

1. **Calculate free gaps**:
   - Before the first meeting
   - Between meetings
   - After the last meeting

2. **Use sliding window**:
   - Find the maximum sum of `k+1` consecutive free gaps
   - This simulates removing `k` meetings to create the largest continuous free time

---
