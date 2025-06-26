class Solution:
    def longestSubsequence(self, s, k):
        n = len(s)
        count = 0       # Counts how many digits we can take
        value = 0       # Current binary value
        power = 1       # 2^0, 2^1, ..., used to calculate the value of bits from right to left

        # Step 1: Start from the right (least significant bit)
        for i in range(n - 1, -1, -1):
            # If it's a '1', check if including it keeps value <= k
            if s[i] == '1':
                if power <= k and value + power <= k:
                    value += power
                    count += 1
                # Increase power (e.g., 2^0 → 2^1 → 2^2 → ...)
                power *= 2
            else:
                # Always include '0's because they don’t add value
                count += 1
                power *= 2

            # Optional speed-up: Stop if power exceeds k
            if power > k:
                break

        # Step 2: Count all leading '0's on the left side we skipped
        # (These are not checked in loop but are free to include)
        for i in range(n - count):
            if s[i] == '0':
                count += 1

        return count
