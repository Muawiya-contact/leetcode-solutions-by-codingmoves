class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        rows = len(strs)
        cols = len(strs[0])
        delete_count = 0

        for col in range(cols):
            for row in range(1, rows):
                if strs[row][col] < strs[row - 1][col]:
                    delete_count += 1
                    break   # no need to check further rows for this column

        return delete_count
