# 2900. Longest Unequal Adjacent Groups Subsequence I

## Problem Statement

You are given:

- A list of **distinct** strings: `words`
- A corresponding list of binary values: `groups` (0s and 1s)

Each word at index `i` belongs to group `groups[i]`.

### Goal:

Find the **longest subsequence** of words where no two **adjacent words** in the subsequence belong to the **same group**. That is, the group values must alternate between 0 and 1.

### Note:

- A **subsequence** means keeping the order but possibly skipping some elements.
- Multiple valid answers can exist. Return any of them.

---

## Examples

### Example 1:

**Input:**
```python
words = ["e", "a", "b"]
groups = [0, 0, 1]
```
### Output:
```
["e", "b"]
```
### Explanation:
+ You can choose "e" (group 0) and "b" (group 1).

+ Or "a" (group 0) and "b" (group 1).

## Constraints
+ `1 <= words.length == groups.length <= 100`

+ Each `words[i]` is a distinct lowercase string of length `1` to `10`.

+ Each `groups[i]` is either `0` or `1`.

## Time Complexity
+ O(n) — We iterate through the list once.

### Space Complexity
+ O(n) — In the worst case, we may store all words in the result.



