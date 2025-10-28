class Solution:
    def countValidSelections(self, nums):
        n = len(nums)
        ans = 0

        # Try every position that has value 0
        for i in range(n):
            if nums[i] != 0:
                continue

            # Try both directions: -1 (left) and +1 (right)
            for direction in [-1, 1]:
                arr = nums[:]  # make a copy
                curr = i
                dirc = direction

                # simulate the process
                while 0 <= curr < n:
                    if arr[curr] == 0:
                        curr += dirc
                    else:
                        arr[curr] -= 1
                        dirc *= -1  # reverse direction
                        curr += dirc

                # check if all became zero
                if all(x == 0 for x in arr):
                    ans += 1

        return ans
