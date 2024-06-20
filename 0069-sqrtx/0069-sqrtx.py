class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x == 1:
            return 1

        mi = -sys.maxint - 1
        ma = sys.maxint

        while mi <= ma:
            mid = (mi + ma) // 2
            sq = mid*mid

            if sq  == x:
                return mid
            
            if sq > x:
                ma = mid - 1
            
            if sq < x:
                if (mid + 1) * (mid+1) > x:
                    return mid
                mi = mid + 1
        
