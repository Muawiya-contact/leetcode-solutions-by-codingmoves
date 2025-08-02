# 2561. Rearranging Fruits
`Hard`
You have two fruit baskets containing n fruits each. You are given two 0-indexed integer arrays basket1 and basket2 representing the cost of fruit in each basket. You want to make both baskets equal. To do so, you can use the following operation as many times as you want:

Chose two indices i and j, and swap the ith fruit of basket1 with the jth fruit of basket2.
The cost of the swap is `min(basket1[i],basket2[j])`.
Two baskets are considered equal if sorting them according to the fruit cost makes them exactly the same baskets.

> Return the minimum cost to make both the baskets equal or -1 if impossible.

### Example 1:

### Input: 
```python
basket1 = [4,2,2,2], basket2 = [1,4,1,2]
```
### Output: 
```python
1
```
### Explanation: 
Swap index 1 of basket1 with index 0 of basket2, which has cost 1. Now basket1 = [4,1,2,2] and basket2 = [2,4,1,2]. Rearranging both the arrays makes them equal.

----
