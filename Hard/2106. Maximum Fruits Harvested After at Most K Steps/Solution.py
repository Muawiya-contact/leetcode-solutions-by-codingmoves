class Solution(object):
    def maxTotalFruits(self, fruits, startPos, k):
        n = len(fruits)
        max_total = 0
        window_sum = 0
        left = 0

        for right in range(n):
            window_sum += fruits[right][1]

            # shrink the window from left if it's not reachable in k steps
            while left <= right:
                left_pos = fruits[left][0]
                right_pos = fruits[right][0]

                min_steps = min(abs(startPos - left_pos), abs(startPos - right_pos)) + (right_pos - left_pos)

                if min_steps > k:
                    window_sum -= fruits[left][1]
                    left += 1
                else:
                    break

            max_total = max(max_total, window_sum)

        return max_total
