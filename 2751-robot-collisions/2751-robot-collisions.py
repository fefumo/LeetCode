class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        """
        :type positions: List[int]
        :type healths: List[int]
        :type directions: str
        :rtype: List[int]
        """
        
        robots = []
        for i in range(len(positions)):
            cur = []
            cur.append(positions[i])
            cur.append(healths[i])
            cur.append(directions[i])
            cur.append(i)
            robots.append(cur)
        
        robots.sort()
        stack = []
        
        for robot in robots:
            if len(stack) == 0 or robot[2] == 'R' or stack[-1][2] == 'L':
                stack.append(robot)
                continue

            if robot[2] == 'L':
                add = True
                while len(stack) > 0 and stack[-1][2] == 'R' and add:
                    stackHp = stack[-1][1]
                    curHp = robot[1]

                    if stackHp == curHp:
                        stack.pop()
                        add = False
                    elif stackHp < curHp:
                        stack.pop()
                        robot[1] -= 1
                    else:
                        stack[-1][1] -= 1
                        add = False
                
                if add:
                    stack.append(robot)

        result = []
        stack.sort(key=lambda robot: robot[3])

        for robot in stack:
            result.append(robot[1])
        
        return result
