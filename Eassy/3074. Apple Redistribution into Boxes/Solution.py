class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        # Step 1: total number of apples
        total_apples = sum(apple)
        
        # Step 2: sort box capacities in descending order
        capacity.sort(reverse=True)
        
        # Step 3: pick boxes until capacity is enough
        used_boxes = 0
        current_capacity = 0
        
        for cap in capacity:
            current_capacity += cap
            used_boxes += 1
            if current_capacity >= total_apples:
                return used_boxes       
