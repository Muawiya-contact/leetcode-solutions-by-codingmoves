from collections import Counter
class Solution:
    def maxFrequency(self,nums, k, numOperations):
        mp = Counter(nums)
        keys = list(mp.keys())
        keys.sort()
        freq = ans = 0
        i = j = 0
        for center in range(keys[0], keys[-1]+1):
            while j < len(keys) and keys[j] <= center+k:
                freq += mp[keys[j]]
                j += 1
            while i < len(keys) and keys[i] < center-k:
                freq -= mp[keys[i]]
                i += 1
            ans = max(ans, min(mp.get(center,0)+numOperations, freq))
        return ans
        
