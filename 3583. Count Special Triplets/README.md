# 3583. Count Special Triplets

You are given an integer array `nums`.

A special triplet is defined as a triplet of indices `(i, j, k)` such that:

+ `0 <= i < j < k < n`, where `n = nums.length`
+ `nums[i] == nums[j] * 2`
+ `nums[k] == nums[j] * 2`
Return the total number of special triplets in the array.

Since the answer may be large, return it modulo `109 + 7`.
