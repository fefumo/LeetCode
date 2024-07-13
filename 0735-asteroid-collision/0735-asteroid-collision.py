class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for i in range(len(asteroids)): 
            if len(stack) == 0 or (stack[-1] < 0 and asteroids[i] > 0) or (stack[-1] < 0 and asteroids[i] < 0) or (stack[-1] > 0 and asteroids[i] > 0):
                stack.append(asteroids[i])
            else:
                while (len(stack) > 0 and stack[-1] > 0 and stack[-1] < abs(asteroids[i])):
                    stack.pop()
                if  len(stack) == 0 or stack[-1] < 0:
                    stack.append(asteroids[i])
                elif stack[-1] == abs(asteroids[i]):
                    stack.pop()
        return stack 