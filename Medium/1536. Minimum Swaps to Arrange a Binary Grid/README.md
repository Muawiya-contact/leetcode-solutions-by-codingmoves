# 1536. Minimum Swaps to Arrange a Binary Grid

**Difficulty:** Medium

---

## Problem Statement

Given an `n x n` binary grid, in one step you can choose two **adjacent rows** of the grid and swap them.

A grid is said to be **valid** if all the cells above the main diagonal are zeros.

Return the **minimum number of steps** needed to make the grid valid, or `-1` if the grid cannot be made valid.

> The **main diagonal** of a grid is the diagonal that starts at cell `(1, 1)` and ends at cell `(n, n)`.

---

## Examples

### Example 1

**Input:**
```
grid = [[0,0,1],
        [1,1,0],
        [1,0,0]]
```
**Output:** `3`

---

### Example 2

**Input:**
```
grid = [[0,1,1,0],
        [0,1,1,0],
        [0,1,1,0],
        [0,1,1,0]]
```
**Output:** `-1`

**Explanation:** All rows are identical, so swaps have no effect on the grid.

---

### Example 3

**Input:**
```
grid = [[1,0,0],
        [1,1,0],
        [1,1,1]]
```
**Output:** `0`

---

## Constraints

| Constraint | Value |
|---|---|
| `n == grid.length == grid[i].length` | — |
| Grid size | `1 <= n <= 200` |
| Cell values | `grid[i][j]` is either `0` or `1` |

---

## Solution (Greedy + Bubble Up)

### Key Insight

For the grid to be valid, row `i` must have at least `n - 1 - i` **trailing zeros**:

| Position | Required Trailing Zeros |
|---|---|
| Row 0 | n - 1 (strictest) |
| Row 1 | n - 2 |
| ... | ... |
| Row n-1 | 0 (easiest) |

### Approach

1. **Count trailing zeros** for each row.
2. **Greedily** find the nearest row (from current position downward) with enough trailing zeros.
3. **Bubble it up** by swapping adjacent rows, counting each swap.
4. If no valid row exists for a position → return `-1`.



### Complexity

| | |
|---|---|
| **Time** | O(n²) |
| **Space** | O(n) |
