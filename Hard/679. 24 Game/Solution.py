class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        # LeetCode 679: 24 Game — Backtracking solution with floating-point tolerance

        from math import isclose
        from itertools import permutations

        nums = [float(x) for x in cards]
        EPS = 1e-6

        def dfs(arr):
            if len(arr) == 1:
                return isclose(arr[0], 24.0, abs_tol=EPS)
                # Try all unordered pairs by index
            n = len(arr)
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                        # build the remainder list
                    rest = [arr[k] for k in range(n) if k != i and k != j]

                    a, b = arr[i], arr[j]

                        # operations to try; for addition and multiplication, enforce i<j to avoid duplicate commutative ops
                    ops = []
                    ops.append(a + b)
                    ops.append(a - b)
                    ops.append(a * b)
                    if abs(b) > EPS:
                        ops.append(a / b)

                    for val in ops:
                        if dfs(rest + [val]):
                            return True
            return False

        return dfs(nums)


        
