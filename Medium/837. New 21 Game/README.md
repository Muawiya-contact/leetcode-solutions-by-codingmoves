# 🎲 LeetCode 837. New 21 Game

## 📌 Problem Statement
Alice plays a game similar to Blackjack (21):

- She starts with **0 points**.  
- As long as her score is **less than `k`**, she draws random numbers.  
- Each draw gives her an integer in the range **[1, maxPts]**, all equally likely.  
- Alice **stops** once her score is **at least `k`**.  
- We need the **probability that her final score is at most `n`**.  

Answers within `1e-5` of the correct answer are accepted.

---

## 🔹 Example 1
**Input:**  
`n = 10, k = 1, maxPts = 10`  

**Output:**  
`1.00000`  

**Explanation:**  
Alice only draws once, getting a number between `1` and `10`.  
In every case, her score ≤ 10, so probability = 1.0.  

---

## 🔹 Example 2
**Input:**  
`n = 6, k = 1, maxPts = 10`  

**Output:**  
`0.60000`  

**Explanation:**  
Possible scores after one draw = {1, 2, …, 10}.  
Out of these, 6 are ≤ 6.  
Probability = `6/10 = 0.6`.  

---

## 🔹 Example 3
**Input:**  
`n = 21, k = 17, maxPts = 10`  

**Output:**  
`0.73278`  

---

## ⚙️ Constraints
- `0 <= k <= n <= 10^4`  
- `1 <= maxPts <= 10^4`  

---

## 🚀 Approach
This is a **Dynamic Programming (DP) + Sliding Window** problem.

### Key Idea:
- Let `dp[i]` = probability of ending with exactly `i` points.  
- Initially, `dp[0] = 1.0` (start with 0 points).  
- For each `i < k`, Alice can move to `i+1 ... i+maxPts`.  
- Each transition has equal probability `1/maxPts`.  
- Once `i ≥ k`, Alice **stops**, so we only sum probabilities for `k ≤ i ≤ n`.

### Optimization:
Instead of recalculating the window sum every time, we use a **sliding window** to keep track of the sum of the last `maxPts` probabilities.

---

