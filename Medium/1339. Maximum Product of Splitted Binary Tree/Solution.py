class Solution:
    def maxProduct(self, root):
        MOD = 10**9 + 7
        self.max_prod = 0
        
        # Step 1: get total sum of tree
        def totalSum(node):
            if not node:
                return 0
            return node.val + totalSum(node.left) + totalSum(node.right)
        
        total = totalSum(root)
        
        # Step 2: compute subtree sums and maximize product
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            sub_sum = node.val + left + right
            self.max_prod = max(self.max_prod, sub_sum * (total - sub_sum))
            
            return sub_sum
        
        dfs(root)
        return self.max_prod % MOD
