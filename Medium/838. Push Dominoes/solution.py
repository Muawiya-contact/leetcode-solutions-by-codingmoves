class Solution(object):
    def pushDominoes(self, dominoes):
        dominoes = list(dominoes)
        n = len(dominoes)
        i = 0
        left = 'L'
        
        while i < n:
            j = i
            while j < n and dominoes[j] == '.':
                j += 1

            right = dominoes[j] if j < n else 'R'

            # Now update dominoes between i-1 and j
            if left == right:
                # Fill with the same direction
                for k in range(i, j):
                    dominoes[k] = left
            elif left == 'R' and right == 'L':
                # Fill inward from both sides
                l, r = i, j - 1
                while l < r:
                    dominoes[l] = 'R'
                    dominoes[r] = 'L'
                    l += 1
                    r -= 1
            # else (L...R) → leave as is

            left = right
            i = j + 1
        
        return ''.join(dominoes)
