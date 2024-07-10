class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        begptr = 0
        curptr = 0
        for i in range(len(logs)):
            if logs[i] == "../" and curptr == 0:
                continue
            elif logs[i] == "../" and curptr != 0:
                curptr -= 1
            elif logs[i] == "./":
                continue
            else:
                curptr += 1
        return curptr - begptr
