class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = set()
        cur = set()

        for num in arr:
            new_cur = {num}
            for prev in cur:
                new_cur.add(prev | num)
            cur = new_cur
            res.update(cur)
        return len(res)
        
