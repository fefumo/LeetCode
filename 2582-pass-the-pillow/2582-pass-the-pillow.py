class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        """
        testcases
        3
        2
        3
        1000
        1000
        101
        873
        874
        23
        967
        10
        999
        18
        38
        2
        1000
        """
        #time to get to the last person: n - 1
        #after (2n-2) it's returned to the first
        #r = 0
        chunks = time // (n - 1)
        return (time % (n - 1) + 1) if chunks % 2 == 0 else (n - time % (n - 1))
            
                
            
            