class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ht = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' :  100, 'D' : 500, 'M' : 1000}
        result = 0
        count = 0
        flag = True
        
        if len(s) == 1:
            return ht.get(s)
        
        for i in range(len(s)-1):
            count += 1
            if flag is not True and count != len(s) - 1:
                flag = True
                continue
            if s[i] == 'I' and s[i+1] == 'V':
                result += 4
                flag = False
            elif s[i] == 'I' and s[i+1] == 'X':
                flag = False
                result += 9
            elif s[i] == 'X' and s[i+1] == 'L':
                flag = False
                result += 40
            elif s[i] == 'X' and s[i+1] == 'C':
                flag = False
                result += 90
            elif s[i] == 'C' and s[i+1] == 'D':
                flag = False
                result += 400
            elif s[i] == 'C' and s[i+1] == 'M':
                flag = False
                result += 900
            else:
                if flag == False and count == len(s) - 1:
                    result += ht.get(s[i+1])
                elif count == len(s)-1:
                    result += ht.get(s[i]) + ht.get(s[i + 1])
                else:
                    result += ht.get(s[i])
        
        return result
        
