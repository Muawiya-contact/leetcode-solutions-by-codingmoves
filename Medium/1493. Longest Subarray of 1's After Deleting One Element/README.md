# 1493. Longest Subarray of 1's After Deleting One Element
**Difficulty:** Medium  
**Topics:** Sliding Window, Two Pointers  

## Problem Statement
You are given a binary array `nums`. You should delete **one element** from it.  
Return the size of the longest non-empty subarray containing only `1`s in the resulting array. Return `0` if there is no such subarray.

## Examples
**Example 1:**  
Input: nums = [1,1,0,1]  
Output: 3  
Explanation: After deleting the number at index 2, we get [1,1,1] which has length 3.  

**Example 2:**  
Input: nums = [0,1,1,1,0,1,1,0,1]  
Output: 5  
Explanation: After deleting the number at index 4, the longest subarray of 1's is [1,1,1,1,1].  

**Example 3:**  
Input: nums = [1,1,1]  
Output: 2  
Explanation: You must delete one element.  

## Constraints
- `1 <= nums.length <= 10^5`  
- `nums[i]` is either `0` or `1`.  

## Approach
We need the longest subarray of 1’s after deleting **one element**. This can be seen as finding the longest window that contains **at most one zero** (since we can delete it).  

Steps:  
1. Use two pointers `left` and `right` to form a sliding window.  
2. Keep a count of zeros inside the window.  
3. If the window has more than one zero, shrink it from the left.  
4. Track the maximum valid window length.  
5. Since one element must be deleted, the answer is `max_len - 1`.  

---------
