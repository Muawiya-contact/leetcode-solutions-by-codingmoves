class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        weeks = n // 7
        days = n % 7
        total = 0

        # Complete weeks
        # Each week starts with (1 + week_index)
        for w in range(weeks):
            total += (7 * (w + 1)) + (7 * 6) // 2  # sum of 7 consecutive days

        # Remaining days
        start = weeks + 1
        for d in range(days):
            total += start + d

        return total
