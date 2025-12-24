# Apple Redistribution into Boxes (LeetCode 3074)

## 📌 Problem Overview

You are given:
- An array `apple` where each element represents the number of apples in a pack.
- An array `capacity` where each element represents the capacity of a box.

Your task is to find the **minimum number of boxes** required to store **all apples**.

### Important Notes
- Apples from the same pack can be split into different boxes.
- Apples from different packs can be stored in the same box.
- It is guaranteed that the total box capacity is sufficient to store all apples.

---

## 🧠 Approach (Simple Explanation)

1. Calculate the **total number of apples**.
2. Sort the box capacities in **descending order**.
3. Start picking the largest boxes first.
4. Keep adding box capacities until the total capacity is **greater than or equal to** the total apples.
5. Count how many boxes were used — that is the answer.

---

