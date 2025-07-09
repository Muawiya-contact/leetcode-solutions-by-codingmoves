class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        """
        :type eventTime: int
        :type k: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        n = len(startTime)
        
        # Step 1: Calculate all gaps (free time between meetings)
        freeArray = [startTime[0]]  # gap before the first meeting
        for i in range(1, n):
            freeArray.append(startTime[i] - endTime[i - 1])
        freeArray.append(eventTime - endTime[-1])  # gap after last meeting

        # Step 2: Sliding window of size (k + 1)
        max_sum = 0
        cur_sum = 0
        i = 0

        for j in range(len(freeArray)):
            cur_sum += freeArray[j]

            if j - i + 1 > k + 1:
                cur_sum -= freeArray[i]
                i += 1

            if j - i + 1 == k + 1:
                max_sum = max(max_sum, cur_sum)

        return max_sum
