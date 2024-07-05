# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        # if head.next == None or head.next.next == None:
        #     return [-1, -1]
        prev = head
        head = head.next
        arr = []
        idx = 0
        while head.next is not None:
            idx += 1
            #maxima
            if head.val > prev.val and head.val > head.next.val:
                arr.append(idx)
            #minima
            if head.val < prev.val and head.val < head.next.val:
                arr.append(idx)
            
            prev = head
            head = head.next

        if len(arr) < 2:
            return [-1, -1]
        max_distance = arr[-1] - arr[0]
        min_distance = sys.maxsize
        
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] < min_distance:
                min_distance = arr[i] - arr[i-1]
        
        return [min_distance, max_distance]