class Solution(object):
    def maxSubsequence(self, nums, k):
        # Step 1: Pair each number with its index
        indexed_nums = list(enumerate(nums))
        
        # Step 2: Sort by value in descending order, pick top k
        top_k = sorted(indexed_nums, key=lambda x: x[1], reverse=True)[:k]
        
        # Step 3: Sort top k by original index to maintain order
        top_k_sorted = sorted(top_k, key=lambda x: x[0])
        
        # Step 4: Extract values only
        return [x[1] for x in top_k_sorted]
