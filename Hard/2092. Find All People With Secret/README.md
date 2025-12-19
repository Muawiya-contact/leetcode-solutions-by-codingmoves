# 2092. Find All People With Secret

## Problem Description

You are given:

- An integer `n` representing the number of people (numbered from `0` to `n-1`).  
- A list of `meetings`, where `meetings[i] = [xi, yi, timei]` indicates that person `xi` and person `yi` have a meeting at `timei`.  
- An integer `firstPerson`, the person who initially receives a secret from person `0` at time `0`.  

**Rules:**

1. Person `0` knows a secret initially and shares it with `firstPerson` at time `0`.  
2. At any meeting, if a person knows the secret, they **instantly share it** with the other person.  
3. Secret spreading is instantaneous within the same time, so chains of meetings at the same time can spread the secret further.  

**Goal:**  
Return a list of all people who know the secret after all meetings.

---

## Example

```python
n = 6
meetings = [[1,2,5],[2,3,8],[1,5,10]]
firstPerson = 1

Output: [0,1,2,3,5]
