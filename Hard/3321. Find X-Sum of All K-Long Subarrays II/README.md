# 3321. Find X-Sum of All K-Long Subarrays II
***Problem Statement:***

You are given an array `nums` of `n` integers and two integers `k` and `x`.

The *x-sum* of an array is calculated by the following procedure:

+ Count the occurrences of all elements in the array.
+ Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
+ Calculate the sum of the resulting array.
  
*Note* that if an array has less than `x` distinct elements, its `x-sum` is the sum of the array.

Return an integer array `answer` of length `n - k + 1` where `answer[i]` is the x-sum of the <a href="#" title = "Subarray
A subarray is a contiguous non-empty sequence of elements within an array.">subarra</a> `nums[i..i + k - 1]`.

------
## Example 1:

### Input: 
```py
nums = [1,1,2,2,3,4,2,3], k = 6, x = 2
```

### Output: 
```py
[6,10,12]
```

## Constraints:

+ `nums.length == n`
+ `1 <= n <= 105`
+ `1 <= nums[i] <= 109`
+ `1 <= x <= k <= nums.length`

---
