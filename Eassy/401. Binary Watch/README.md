# 401. Binary Watch

## 🧠 Problem Summary

A binary watch has:

- 4 LEDs for the **hour** (0–11)
- 6 LEDs for the **minutes** (0–59)

Each LED represents a binary bit (0 or 1).

You are given an integer `turnedOn` which represents the total number of LEDs that are ON.

Your task is to return all possible valid times the watch could display with exactly `turnedOn` LEDs ON.

---

## ⚠️ Important Rules

- Hour must be between **0 and 11**
- Minute must be between **0 and 59**
- Hour must NOT have leading zero  
  - ❌ `01:00`  
  - ✅ `1:00`
- Minute must always have 2 digits  
  - ❌ `10:2`  
  - ✅ `10:02`

---

## 💡 Approach

We try all possible hours and minutes:

- Hours → `0 to 11`
- Minutes → `0 to 59`

For each pair:
- Count number of `1`s in binary form of hour
- Count number of `1`s in binary form of minute
- If total equals `turnedOn`, add it to result

Since total combinations are:

`12 × 60 = 720`
