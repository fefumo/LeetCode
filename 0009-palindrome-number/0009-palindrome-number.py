class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        sx = str(x)
        end = -1
        for i in range(len(sx)/2):
            if sx[i] != sx[end]:
                return False
            end -= 1
        
        return True
