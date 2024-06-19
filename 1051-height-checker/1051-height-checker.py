class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        count = 0
        sorted = False
        copy = list(heights)
        while sorted != True:
            for i in range(len(copy)):
                for j in range(len(copy) - 1):
                    if copy[j] > copy[j+1]:
                        copy[j], copy[j+1] = copy[j+1], copy[j]
            sorted = True
        
        for i in range(len(copy)):
            if copy[i] != heights[i]:
                count += 1
        return count