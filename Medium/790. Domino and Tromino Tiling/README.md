# 790. Domino and Tromino Tiling
**Medium**  
**Topics:** Dynamic Programming

## Problem Description

You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.

Given an integer `n`, return the number of ways to tile a `2 x n` board. Since the answer may be very large, return it modulo \(10^9 + 7\).

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

## Example 1:
### Input:
```
n = 3
```
### Output:
```
5
```
### Explanation:
The five different ways to tile the board are:

1. 3 vertical dominoes
2. 1 horizontal domino + 2 vertical dominoes
3. 1 tromino covering one row + remaining filled appropriately
4. Another tromino variation (rotated)
5. Another tromino variation (flipped)
6. 
### Constraints:
- \( 1 \leq n \leq 1000 \)

## Approach

We will use dynamic programming to solve this problem efficiently. The main idea is to define `dp[i]` as the number of ways to tile a `2 x i` board.

### Base Cases:
- `dp[0] = 1` (1 way to tile an empty board)
- `dp[1] = 1` (Only one way to tile a `2 x 1` board with a vertical domino)
- `dp[2] = 2` (Two ways to tile a `2 x 2` board with either two vertical dominoes or two horizontal dominoes)

### Recurrence Relation:
For `n >= 3`, the recurrence relation is:
```
dp[i] = dp[i-1] + dp[i-2] + 2 * dp[i-3]
```
- `dp[i-1]`: Add a vertical domino to the board
- `dp[i-2]`: Add two horizontal dominoes to the board
- `2 * dp[i-3]`: Add L-shaped trominoes (two symmetrical placements)

 # Explanation of the Code

### Base Cases:
We handle small values of `n` directly:
- `dp[0] = 1`: One way to tile an empty board.
- `dp[1] = 1`: One way to tile a `2 x 1` board (with a vertical domino).
- `dp[2] = 2`: Two ways to tile a `2 x 2` board (either two vertical dominoes or two horizontal dominoes).

These base cases handle the smallest possible board sizes and are essential to kickstart the dynamic programming approach for larger values of `n`.

### Dynamic Programming:
For `i >= 3`, we calculate `dp[i]` using the recurrence relation:
```
dp[i] = dp[i-1] + dp[i-2] + 2 * dp[i-3]
```
This relation works because:
- `dp[i-1]` represents the case where we add a vertical domino to the board, reducing the problem to tiling a `2 x (i-1)` board.
- `dp[i-2]` accounts for placing two horizontal dominoes to tile the board.
- `2 * dp[i-3]` accounts for placing two types of L-shaped trominoes, giving us two symmetrical ways of placing them.

To calculate the values of `dp[i]` efficiently, we use `preSum`, which stores the sum of relevant previous `dp` values (specifically the sum of `dp[0]` to `dp[i-3]`). This helps avoid recalculating the sum repeatedly.

### Time Complexity:
The time complexity is \(O(n)\) because we only loop from `3` to `n` to fill in the `dp` array. We only perform constant time operations for each iteration, and the loop runs `n-2` times.

### Space Complexity:
The space complexity is \(O(n)\) because we store the values of `dp[i]` for all `i` from `0` to `n` in the `dp` array. The extra space used is linear with respect to `n`.

### Final Thoughts:
This problem is a great example of how dynamic programming can be applied to tiling problems. The efficient approach using `preSum` helps avoid recalculating the sum of previous `dp` values, reducing redundant calculations and improving performance.

The solution is both time-efficient and space-efficient, making it a good example of solving a combinatorial tiling problem using dynamic programming.
 
