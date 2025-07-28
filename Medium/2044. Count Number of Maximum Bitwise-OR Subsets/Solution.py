class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.max_or = 0
        self.count = 0
        
        def dfs(index, current_or):
            if index == len(nums):
                if current_or == self.max_or:
                    self.count += 1
                elif current_or > self.max_or:
                    self.max_or = current_or
                    self.count = 1
                return
            
            # include nums[index] in subset
            dfs(index + 1, current_or | nums[index])
            
            # exclude nums[index] from subset
            dfs(index + 1, current_or)
        
        dfs(0, 0)
        return self.count
