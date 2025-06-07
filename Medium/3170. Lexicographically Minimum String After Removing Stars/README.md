# 🧩 LeetCode 3170 - Lexicographically Minimum String After Removing Stars

## 💡 Problem Statement

You are given a string `s` which may contain any number of `'*'` characters.

Your task is to remove all `'*'` characters.  
Each time you remove a `'*'`, you must also delete the **smallest non-'*' character to its left**. If there are multiple occurrences of the smallest character, you can remove **any one** of them.

You must return the **lexicographically smallest** resulting string after performing all such deletions.

---

## 🧪 Example

### Example 1:
### Input: 
```text
s = "aabb*df"
```
### Output:
```text
"abdf"
```
### Explanation: 
The first `*` deletes one `'a'` and itself. Remaining string: `"abdf"`

---
### 🔄 Approach
  + Use a min-heap `(heapq)` to always know the smallest character to the left of each `'*'`.
  
  + Use a `defaultdict(deque)` to map each character to the positions it appears at.
  
  + Keep a list `keep[]` to mark whether a character should stay in the final string.
  
  + Traverse the input string:
  
    + If the character is not `*`, push it to the heap and record its index.
    
    + If the character is `*`, pop the smallest character from the heap, and mark both it and the `*` for removal.

 ---
 ### 🧠 Time and Space Complexity
  + Time Complexity: `O(n log n)`
  
    + Each `heapq` operation is `log n`
    
    + We process each character once
    
  + Space Complexity: `O(n)`
  
    + Heap + index map + result array

---
      
  
  
