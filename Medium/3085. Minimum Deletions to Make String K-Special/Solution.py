import collections

class Solution(object):
    def minimumDeletions(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        count = collections.Counter(word)
        freq_list = list(count.values())
        freq_list.sort()
        min_deletions = float('inf')  # fix: initialize to large value

        for target_freq in freq_list:
            deletions = 0
            for freq in freq_list:
                if freq < target_freq:
                    deletions += freq  # delete all to skip it
                elif freq > target_freq + k:
                    deletions += freq - (target_freq + k)  # delete extras to make within range
            min_deletions = min(min_deletions, deletions)  # fix: update inside loop

        return min_deletions

# Test
obj = Solution()
print(obj.minimumDeletions("aaabaaa", k=2))  # Output should be 1
