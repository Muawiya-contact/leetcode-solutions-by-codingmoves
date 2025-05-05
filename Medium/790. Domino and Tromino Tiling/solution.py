class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5
        
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2
        preSum = 1  # Stores dp[0] + dp[1] + ... + dp[i-3]
        
        for i in range(3, n + 1):
            dp[i] = (2 * preSum + dp[i - 1] + dp[i - 2]) % MOD
            preSum = (preSum + dp[i - 2]) % MOD
        
        return dp[n]
