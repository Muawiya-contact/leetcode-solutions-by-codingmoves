# Maximum Running Time of N Computers

## Problem Description

You are given `n` computers and a list of `batteries` representing their capacities. Each battery can power a computer for a certain amount of time. Your task is to determine the **maximum running time** that all `n` computers can simultaneously run using these batteries. Batteries can be combined but cannot be split.

---

## Approach

The solution uses a **greedy approach**:

1. **Sort the batteries** in ascending order.
2. Separate the **largest `n` batteries** to assign to the `n` computers initially.
3. Calculate the **extra power** from remaining batteries:  
   ```python
   extra = sum(batteries[:-n])
```
