import heapq

class TaskManager(object):

    def __init__(self, tasks):
        """
        :type tasks: List[List[int]]
        """
        self.task_map = {}  # taskId -> (priority, userId)
        self.heap = []      # entries: (-priority, -taskId, userId, taskId)
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId, taskId, priority):
        """
        :type userId: int
        :type taskId: int
        :type priority: int
        :rtype: None
        """
        self.task_map[taskId] = (priority, userId)
        heapq.heappush(self.heap, (-priority, -taskId, userId, taskId))

    def edit(self, taskId, newPriority):
        """
        :type taskId: int
        :type newPriority: int
        :rtype: None
        """
        # taskId guaranteed to exist
        userId = self.task_map[taskId][1]
        self.task_map[taskId] = (newPriority, userId)
        heapq.heappush(self.heap, (-newPriority, -taskId, userId, taskId))

    def rmv(self, taskId):
        """
        :type taskId: int
        :rtype: None
        """
        if taskId in self.task_map:
            del self.task_map[taskId]

    def execTop(self):
        """
        :rtype: int
        """
        while self.heap:
            negPriority, negTaskId, heapUserId, taskId = heapq.heappop(self.heap)
            # skip if task no longer exists
            if taskId not in self.task_map:
                continue
            curPriority, curUserId = self.task_map[taskId]
            # validate both priority and user match current record
            if curPriority == -negPriority and curUserId == heapUserId:
                del self.task_map[taskId]  # remove after execution
                return curUserId
            # else stale entry, continue popping
        return -1
