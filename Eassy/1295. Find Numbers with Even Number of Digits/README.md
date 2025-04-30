# LeetCode Problem 1295: Find Numbers with Even Number of Digits

## 🧩 Problem Description

Given an array `nums` of integers, return how many of them contain an **even number of digits**.

### 🔢 Example 1:
### Input: 
```
nums = [12, 345, 2, 6, 7896]
```
### Output: 
`2`
### Explanation:
+ `12` contains `2` digits (even)
+ `345` contains `3` digits (odd)
+ `2` contains `1` digit (odd)
+ `6` contains `1` digit (odd)
+ `7896` contains `4` digits (even)
+ 
=> Result: `2` numbers have even number of digits

---

## ✅ Constraints

- `1 <= nums.length <= 500`  
- `1 <= nums[i] <= 10^5`

---

## 🧠 Solution (Python)

```python
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                count += 1
        return count
```
## ✅ Test Case
```
obj = Solution()
print(obj.findNumbers([1, 22, 3, 33, 33]))  # Output: 3
```
## 🚀 Optimized Version (One-Liner)
```
class Solution:
    def findNumbers(self, nums):
        return sum(1 for i in nums if len(str(i)) % 2 == 0)

```
## 📊 Complexity
+ Time Complexity: O(n), where n is the number of elements in nums
+ Space Complexity: O(1), using constant extra space

## 💡 Tip
Converting numbers to strings is a simple and readable way to count digits. For performance-critical tasks, you could also use `math.log10()` and `int` to count digits without string conversion.


