class Solution(object):
    def areSimilar(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        n = len(mat[0])
        shift = k % n
        
        for i in range(len(mat)):
            
            if i % 2 == 0:  # even row → left shift
                if mat[i] != mat[i][shift:] + mat[i][:shift]:
                    return False
            
            else:  # odd row → right shift
                if mat[i] != mat[i][-shift:] + mat[i][:-shift]:
                    return False
        
        return True
