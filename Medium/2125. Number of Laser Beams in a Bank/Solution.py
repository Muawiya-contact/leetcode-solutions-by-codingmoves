class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        prev_devices = 0
        beams = 0
        
        for row in bank:
            curr_devices = row.count('1')
            if curr_devices > 0:
                beams += prev_devices * curr_devices
                prev_devices = curr_devices
                
        return beams
