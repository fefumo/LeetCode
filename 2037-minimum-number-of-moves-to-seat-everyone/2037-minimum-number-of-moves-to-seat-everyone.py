class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        count = 0
        students.sort()
        seats.sort()
        for i in range(len(students)):
            count += abs(students[i] - seats[i])
        
        return count



    def abs(x):
        if x >= 0:
            return x
        else:
            return -x