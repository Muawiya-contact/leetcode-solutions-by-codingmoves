class Solution(object):
    def sumFourDivisors(self, nums):
        total_sum = 0

        for num in nums:
            divisors = []

            for j in range(1, int(num**0.5) + 1):
                if num % j == 0:
                    divisors.append(j)
                    if j != num // j:
                        divisors.append(num // j)

            if len(divisors) == 4:
                total_sum += sum(divisors)

        return total_sum
        
