class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        r = numBottles
        cur_bottles = numBottles
        while cur_bottles // numExchange > 0:
            left = cur_bottles % numExchange
            exchanged = cur_bottles // numExchange
            r += exchanged
            cur_bottles = exchanged + left
        return r