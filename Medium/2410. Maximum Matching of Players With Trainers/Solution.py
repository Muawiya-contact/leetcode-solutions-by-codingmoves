class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
 
        players.sort()
        trainers.sort()
        
        child = 0  # pointer for players (children)
        cookie = 0  # pointer for s (cookies)
        
        while child < len(players) and cookie < len(trainers):
            if trainers[cookie] >= players[child]:
                # Cookie can satisfy the child
                child += 1
            # Move to next cookie either way
            cookie += 1
        
        return child  # Number of content children
    
