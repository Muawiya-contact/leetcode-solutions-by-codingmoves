class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        total_time = 0
        max_time_in_group = neededTime[0]

        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                # Add smaller one to total, keep max
                total_time += min(max_time_in_group, neededTime[i])
                # Update max to compare with next one in same group
                max_time_in_group = max(max_time_in_group, neededTime[i])
            else:
                # new color group, reset max
                max_time_in_group = neededTime[i]
        
        return total_time


