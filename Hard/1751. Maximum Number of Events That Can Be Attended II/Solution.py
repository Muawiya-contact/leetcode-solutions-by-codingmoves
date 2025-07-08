class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Sort events by start time
        events.sort()
        
        # Cache for memoization
        @lru_cache(None)
        def dp(index, count):
            if index == len(events) or count == 0:
                return 0
            
            # Binary search: find next event that starts after current ends
            next_index = bisect.bisect_right(events, events[index][1], key=lambda x: x[0])
            
            # Option 1: skip current event
            skip = dp(index + 1, count)
            
            # Option 2: take current event, and jump to next non-overlapping one
            take = events[index][2] + dp(next_index, count - 1)
            
            return max(skip, take)
        
        return dp(0, k)
