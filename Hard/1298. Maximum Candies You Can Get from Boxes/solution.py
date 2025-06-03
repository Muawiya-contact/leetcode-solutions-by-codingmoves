from collections import deque

class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        """
        :type status: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :rtype: int
        """
        queue = deque()
        owned_boxes = set(initialBoxes)
        available_keys = set()
        visited = set()
        total_candies = 0

        # Add all initially open boxes to the queue
        for box in initialBoxes:
            if status[box] == 1:
                queue.append(box)

        while queue:
            box = queue.popleft()
            if box in visited:
                continue
            visited.add(box)

            # Collect candies
            total_candies += candies[box]

            # Collect new keys
            for key in keys[box]:
                if key not in available_keys:
                    available_keys.add(key)
                    # If you now have the key to a box you already own and it's not opened yet
                    if key in owned_boxes and key not in visited:
                        queue.append(key)

            # Collect new boxes
            for new_box in containedBoxes[box]:
                owned_boxes.add(new_box)
                if status[new_box] == 1 or new_box in available_keys:
                    queue.append(new_box)

        return total_candies
