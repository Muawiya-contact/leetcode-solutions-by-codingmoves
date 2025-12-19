class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        """
        :type n: int
        :type meetings: List[List[int]]
        :type firstPerson: int
        :rtype: List[int]
        """
        from collections import defaultdict, deque
        secret_people = set([0, firstPerson])
        
        # Group meetings by time
        time_to_meetings = defaultdict(list)
        for x, y, t in meetings:
            time_to_meetings[t].append((x, y))
        
        # Process meetings in order of time
        for t in sorted(time_to_meetings.keys()):
            graph = defaultdict(list)
            for x, y in time_to_meetings[t]:
                graph[x].append(y)
                graph[y].append(x)
            
            # Find people connected at this time who already know the secret
            visited = set()
            for person in graph:
                if person in secret_people and person not in visited:
                    # BFS to spread the secret among connected people at this time
                    queue = deque([person])
                    while queue:
                        p = queue.popleft()
                        visited.add(p)
                        secret_people.add(p)
                        for nei in graph[p]:
                            if nei not in visited:
                                queue.append(nei)
        
        return list(secret_people)
