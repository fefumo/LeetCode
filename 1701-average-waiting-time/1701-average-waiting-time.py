class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        timeSpent = 0
        times = []
        first = False
        for customer in customers:
            if timeSpent < customer[0] and first == False:
                timeSpent += customer[0]
                timeSpent += customer[1]
                first = True
            elif timeSpent < customer[0] and first == True:
                timeSpent = customer[0]
                timeSpent += customer[1]
            else:
                timeSpent += customer[1]
            times.append(timeSpent - customer[0])
        s = sum(times)
        return s*1.0 / len(customers)
    
#print(Solution().averageWaitingTime([[5,2], [5,4], [10,3], [20,1]]))