class Solution(object):
    def minTimeToReach(self, moveTime):
        """
        :type moveTime: List[List[int]]
        :rtype: int
        """
        n =len(moveTime)
        m = len(moveTime[0])
        dist = [[float('inf')] * m for _  in range(n)]
        dist[0][0] = 0

        #Priority queue: (time, row, col)
        qu = [(0, 0, 0)]
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        while qu:
            t, row, col = heapq.heappop(qu)

            if row == n-1 and col == m-1:
                return t

            for dx, dy in directions:
                n_row = row + dx
                n_col = col + dy

                if 0 <= n_row < n and 0 <= n_col < m:
                    diff = max(t, moveTime[n_row][n_col]) + 1

                    if diff < dist[n_row][n_col]:
                        dist[n_row][n_col] = diff
                        heapq.heappush(qu, (diff, n_row, n_col))

        return -1                
        
