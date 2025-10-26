# 🏦 LeetCode 2043 — Simple Bank System

## 🧩 Problem Description
You are tasked with writing a program for a bank that automates all its incoming transactions — **transfer**, **deposit**, and **withdraw**.

The bank has `n` accounts, numbered from **1 to n**.  
The initial balance of each account is stored in a 0-indexed array `balance`, where the balance of account `i + 1` is `balance[i]`.

### Valid Transaction Conditions
A transaction is considered valid if:
1. The account number(s) are between **1 and n**.
2. The amount of money withdrawn or transferred is **≤ the account’s balance**.

---

