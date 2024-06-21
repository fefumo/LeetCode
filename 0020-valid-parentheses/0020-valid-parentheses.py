class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        if len(s) == 1:
            return False


        for i in range(len(s)):
            cur = s[i]
            if len(stack) == 0 and (cur == ')' or cur == '}' or cur == ']'):
                return False
            if cur == '(' or cur == '[' or cur == '{':
                stack.append(s[i])
            else:
                if cur == ')' and stack.pop() != '(':
                    return False
                elif cur == '}' and stack.pop() != '{':
                    return False
                elif cur == ']' and stack.pop() != '[':
                    return False
        if len(stack) != 0:
            return False
        return True