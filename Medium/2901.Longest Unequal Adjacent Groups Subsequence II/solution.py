class Solution(object):
    def getWordsInLongestSubsequence(self, words, groups):
        n = len(words)
        dp = [[] for _ in range(n)]

        for i in range(n):
            dp[i] = [i]

        def is_hamming_dist_one(w1, w2):
            if len(w1) != len(w2):
                return False
            diff = 0
            for a, b in zip(w1, w2):
                if a != b:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1

        for i in range(n):
            for j in range(i):
                if groups[j] != groups[i] and is_hamming_dist_one(words[j], words[i]):
                    if len(dp[j]) + 1 > len(dp[i]):
                        dp[i] = dp[j] + [i]

        longest_seq = max(dp, key=len)
        return [words[i] for i in longest_seq]
