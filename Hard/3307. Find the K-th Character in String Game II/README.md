# 🧩 3307. Find the K-th Character in String Game II

## 🚀 Problem Description

Alice and Bob are playing a game. Initially, Alice has a string:

`word = "a"`

They are given a list of operations, and each operation updates the string in one of the following ways:

### 🎮 Operations:

- `0`: Append the string to itself  
  `word = word + word`
  
- `1`: Append the "next character" version of the string  
  Each character in the word is replaced by its next alphabet character (`z` wraps to `a`)  
  Example: `"ab"` → `"bc"` → `word = word + "bc"`

You are given:
- A positive integer `k`  
- A list of operations `operations`

Your task is to **return the `k-th` character** of the final string after performing all operations.

### 🔒 Constraints:

- `1 <= k <= 10^14`
- `1 <= operations.length <= 100`
- `operations[i] ∈ {0, 1}`
- It's guaranteed that the final string will be **at least `k` characters long**

---

## 🧠 Intuition

- Instead of building the whole string (which can be **extremely large**), we simulate the **length changes only**.
- Then we **trace backward** to find the original character and count how many times it was **"shifted"** by op-1 operations.

---

## ✅ Example 1

```python
k = 5
operations = [0, 0, 0]
Operations:

"a" → "aa" → "aaaa" → "aaaaaaaa"
k-th character (5): "a"
```
### Output:
```

"a"
```
