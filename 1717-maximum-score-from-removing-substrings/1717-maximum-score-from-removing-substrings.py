class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        def remove_and_score(s, first, second, score):
            stack = []
            total_score = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    total_score += score
                else:
                    stack.append(char)
            return ''.join(stack), total_score
        
        if x > y:
            s, score_ab = remove_and_score(s, 'a', 'b', x)
            _, score_ba = remove_and_score(s, 'b', 'a', y)
        else:
            s, score_ba = remove_and_score(s, 'b', 'a', y)
            _, score_ab = remove_and_score(s, 'a', 'b', x)
        
        return score_ab + score_ba