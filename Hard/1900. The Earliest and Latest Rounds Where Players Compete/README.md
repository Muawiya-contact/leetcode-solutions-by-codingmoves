# 🏆 Leetcode 1900: The Earliest and Latest Rounds Where Players Compete

## 🔗 Problem Link
[Leetcode 1900](https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/) (Hard)

---

## 🧠 Problem Description

There is a tournament with `n` players arranged in a line from `1` to `n`. In each round:

- The first player plays the last.
- The second player plays the second last.
- And so on...

If there’s an **odd number** of players, the middle one automatically advances.

The winners move to the next round, **sorted again by their original player numbers**.

You are given two players: `firstPlayer` and `secondPlayer`, who **always win** their matches unless they face each other.

Your task is to determine:

- The **earliest** round they can meet
- The **latest** round they can meet

---

## 🧾 Constraints

- `2 <= n <= 28`
- `1 <= firstPlayer < secondPlayer <= n`

---

## 📥 Input

```python
n = 11
firstPlayer = 2
secondPlayer = 4
```
## 📤 Output
```python
[3, 4]
```
## 🔍 Explanation
The players `2` and `4` can meet:

  + As early as round `3` if they both win and reach each other quickly.
  
  + As late as round `4` if others win in such a way that delays their match.
