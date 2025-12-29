from collections import defaultdict

class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        # Step 1: Create a map from bottom pairs to possible top blocks
        allowed_map = defaultdict(list)
        for pattern in allowed:
            key = pattern[:2]  # first two letters = bottom pair
            value = pattern[2] # third letter = top block
            allowed_map[key].append(value)

        # Step 2: Recursive function to build pyramid
        def can_build(current_row):
            # Base case: reached the top
            if len(current_row) == 1:
                return True
            
            # Generate all possible next rows
            next_rows = ['']  # start with empty string
            
            for i in range(len(current_row) - 1):
                pair = current_row[i:i+2]  # take two adjacent blocks
                if pair not in allowed_map:
                    return False  # no allowed pattern for this pair
                
                # Expand all possible next rows
                new_next_rows = []
                for prev in next_rows:
                    for top in allowed_map[pair]:
                        new_next_rows.append(prev + top)
                next_rows = new_next_rows
            
            # Recursively check all possible next rows
            for row in next_rows:
                if can_build(row):
                    return True
            
            return False

        # Start recursion from the bottom
        return can_build(bottom)


# Example usage:
sol = Solution()
print(sol.pyramidTransition("BCD", ["BCC","CDE","CEA","FFF"]))  # True
print(sol.pyramidTransition("AAAA", ["AAB","AAC","BCD","BBE","DEF"]))  # False
