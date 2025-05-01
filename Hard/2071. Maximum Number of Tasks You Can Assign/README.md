# 2071.Maximum Number of Tasks You Can Assign

## Problem Statement

You are given:

- An array `tasks` where `tasks[i]` is the strength required to complete the i-th task.
- An array `workers` where `workers[j]` is the strength of the j-th worker.
- `pills` magical pills, each increasing a worker’s strength by a fixed value `strength`.

Each worker can:
- Be assigned at most **one** task.
- Be given at most **one** pill.

Return the **maximum number of tasks** that can be completed under these constraints.

---

## Example

### Input
```python
tasks = [3, 2, 1]
workers = [0, 3, 3]
pills = 1
strength = 1
```
### Output
```
3
```
### Explanation
+ Give the pill to worker 0, making their strength 1.

+ Assign tasks 1, 2, and 3 to the workers accord

### Constraints
+ `1 <= tasks.length, workers.length <= 5 * 10^4`

+ `0 <= pills <= workers.length`

+ `0 <= tasks[i], workers[j], strength <= 10^9  `

### Algorithm
This solution uses Binary Search + Greedy + Bisect.

#### Steps:
1. Sort the tasks and workers.

2. Use binary search to find the maximum number of tasks k that can be assigned.

3. For each `k`, simulate:

  + Take the hardest `k` tasks.
  
  + Take the strongest `k` workers.
  
  + Try to match them greedily:
  
    + If the strongest available worker can do the task, assign.
  
    + Otherwise, use a pill on the weakest eligible worker.

4. If possible, try more tasks. Otherwise, reduce.

## Complexity Analysis

**Time Complexity:** `O(n log n + m log m + log(min(n, m)) * k)`

- Sorting takes `O(n log n + m log m)`
- Each binary search step takes `O(k log k)`, where `k` is the number of tasks being tested in the mid-range.

**Space Complexity:** `O(k)`  
- This is due to the temporary list `avail` which stores the strongest `k` workers during each binary search simulation.
 


