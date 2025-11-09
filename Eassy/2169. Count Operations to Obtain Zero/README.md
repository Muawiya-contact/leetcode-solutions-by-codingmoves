# Count Operations to Obtain Zero

This Python solution calculates the number of operations required to reduce either of two non-negative integers to zero. In each operation, subtract the smaller number from the larger (or either if equal).

## Problem

Given two non-negative integers `num1` and `num2`, perform the following operation until one becomes zero:

- If `num1 >= num2`, subtract `num2` from `num1`.
- Else, subtract `num1` from `num2`.

Return the total number of operations performed.

