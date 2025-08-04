from collections import defaultdict
class Solution(object):
    def totalFruit(self,fruits):
        count = defaultdict(int)  # to count fruit types
        left = 0
        max_fruits = 0

        for right in range(len(fruits)):
            count[fruits[right]] += 1  # pick fruit at position right

            # If more than 2 types of fruits → shrink window from the left
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]  # remove type if count is 0
                left += 1  # move the window start to the right

            # Update max fruits picked so far
            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
