# Leetcode 2402 – Meeting Rooms III 🏢

## Problem Description

You are given `n` rooms numbered from `0` to `n - 1` and a list of meetings, where each meeting is represented as `[start, end)`. Your goal is to assign each meeting to a room using the following rules:

### 🧠 Rules for Assigning Meetings:
1. **Greedy Room Selection:**  
   Assign each meeting to the **lowest-numbered available room**.

2. **Delay if Necessary:**  
   If no room is free at the meeting's start time, **delay the meeting** until the earliest room becomes free. The meeting keeps its original duration.

3. **Earliest Priority:**  
   If multiple delayed meetings are waiting, assign rooms to meetings with **earlier original start times**.

### 🔁 Objective:
Return the **room number that hosted the most meetings**.  
If there's a tie, return the **lowest room number**.

---

## 🔢 Examples

### Example 1:
**Input:**  
`n = 2`  
`meetings = [[0,10],[1,5],[2,7],[3,4]]`  

**Output:**  
`0`

**Explanation:**
- Meeting 0 → Room 0 at time 0  
- Meeting 1 → Room 1 at time 1  
- Meeting 2 → Delayed → Room 1 at time 5  
- Meeting 3 → Delayed → Room 0 at time 10  

---
## 🧠 Approach
### ✅ Data Structures and Algorithms Used
 + Greedy: Always try to assign a meeting to the earliest and smallest-numbered room.
  
 + Simulation: Track when each room becomes available.
  
 + Optional Optimized Version Uses:
  
  + Min-Heap (Priority Queue) for:
  
   + Available rooms (sorted by room number)
  
   + Busy rooms (sorted by end time)
  
+ Sorting: Meetings are sorted by start time.

  ----
