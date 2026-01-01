class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """

        :type dominoes: List[List[int]]
        :rtype: int
        """
        count_map = {}
        result = 0

        for a, b in dominoes:
            key = tuple(sorted((a,b)))

            if key in count_map:
                result += count_map[key]          
                count_map[key] += 1
            else:
                count_map[key] = 1

        return  result             
