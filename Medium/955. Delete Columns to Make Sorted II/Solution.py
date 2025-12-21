class Solution(object):
    def minDeletionSize(self,strs):
        n = len(strs)
        m = len(strs[0])
        deleted = 0
        sorted_pairs = [False] * (n - 1)
        
        for c in range(m):
            delete_col = False
            for i in range(n - 1):
                if not sorted_pairs[i] and strs[i][c] > strs[i+1][c]:
                    delete_col = True
                    break
            
            if delete_col:
                deleted += 1
                continue
            
            for i in range(n - 1):
                if strs[i][c] < strs[i+1][c]:
                    sorted_pairs[i] = True
        
        return deleted
