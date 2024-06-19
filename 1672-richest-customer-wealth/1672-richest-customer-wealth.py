class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        m = 0
        cur = 0
        for i in range(len(accounts)):
            cur = 0
            for j in range(len(accounts[i])):
               cur += accounts[i][j] 
               m = max(m, cur)
        return m