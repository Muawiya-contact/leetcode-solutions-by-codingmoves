# 3289. The Two Sneaky Numbers of Digitville
**Problem Statement**
In the town of Digitville, there was a list of numbers called `nums` containing integers from `0` to `n - 1`. Each number was supposed to appear exactly once in the list, however, two mischievous numbers sneaked in an additional time, making the list longer than usual.

As the town detective, your task is to find these two sneaky numbers. Return an array of size two containing the two numbers (in any order), so peace can return to Digitville.

---

## Example 1:

### Input: 
```py
nums = [0,1,1,0]
```

### Output: 
```py
[0,1]
```

### Explanation:

> The numbers `0` and `1` each appear twice in the array.

---
## Constraints:

+ `2 <= n <= 100`
+ `nums.length == n + 2`
+ `0 <= nums[i] < n`
+ The input is generated such that `nums` contains exactly two repeated elements.
