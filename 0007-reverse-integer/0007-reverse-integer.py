class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x > 2**32 - 1 or x < -2**32:
            return 0  
        
        string = str(x)
        if string[0] == '-':
            string = '-' + string[:0:-1]
        else:
            string = string[::-1]
            
        if int(string) > (2**31 - 1) or int(string) < -2**31:
            return 0  
        
        return int(string)