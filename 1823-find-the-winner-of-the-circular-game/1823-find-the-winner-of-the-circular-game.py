class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        l = []
        for i in range(1,n+1):
            l.append(i)
        
        cur_idx = 0
        while len(l) != 1:
            cur_idx = (cur_idx + k - 1) % len(l)
            l.pop(cur_idx)
                
        return l[0]
 