import bisect

class Solution(object):
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        m = len(potions)
        result = []
        for s in spells:
            # integer-safe ceiling of success / s
            needed = (success + s - 1) // s
            idx = bisect.bisect_left(potions, needed)
            result.append(m - idx)
        return result
