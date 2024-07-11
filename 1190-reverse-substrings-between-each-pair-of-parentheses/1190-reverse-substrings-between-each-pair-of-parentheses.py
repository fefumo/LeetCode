class Solution(object):
    def __init__(self):
        self.i = 0

    def reverseParentheses(self, s):
        def helper(s):
            sb = []

            while self.i < len(s):
                if s[self.i] == ')':
                    self.i += 1
                    return ''.join(sb)[::-1]
                elif s[self.i] == '(':
                    self.i += 1
                    st = helper(s)
                    sb.append(st)
                else:
                    sb.append(s[self.i])
                    self.i += 1

            return ''.join(sb)

        return helper(s)
        