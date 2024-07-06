class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        #1.Whitespace
        s = s.strip()

        #kekw
        if len(s) == 0:
            return 0
        #first symbol
        if s[0].isdigit() == False:
            if s[0] == '-' or s[0] == '+':
                pass
            else:
                return 0
        #2.Signedness
        idx = 0
        positive = False
        plused = False
        if s[0] == '-':
            idx = 1
        elif s[0] == '+':
            plused = True
            positive = True
        else:
            positive = True
        
        
        new_s = ""

        #3.Convergion
        minus_count = 0
        plus_count = 0
        for c in s:
            if c == '-' :
                minus_count += 1
            if c =='+':
                plus_count += 1
            #gl reading that sh*t)
            if (c.isdigit() == False and  c != '-' and c != '+') or minus_count > 1 or plus_count > 1 or (c == '-' and positive == True) or (c == '+' and positive  == False) or (c =='+' and plused == False):
                break
            new_s += c
        
        if len(new_s) == 0 or new_s == '+' or new_s == '-':
            return 0
        if int(new_s) == 0:
            return 0
        
        #4.Rounding
        if int(new_s)> 2**31 - 1:
            res = 2**31 - 1
        elif int(new_s) < -2**31:
            res = -2**31
        else:
            res = int(new_s)
        
        return res 