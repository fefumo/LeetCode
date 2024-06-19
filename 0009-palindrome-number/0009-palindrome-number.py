class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        orig = x
        new = 0
        while x > 0:
            new = new * 10 + x % 10
            x //= 10

        return new == orig
