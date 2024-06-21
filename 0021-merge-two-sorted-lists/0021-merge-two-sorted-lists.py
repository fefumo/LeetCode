# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0, None)
        tail = dummy
        while True:
            
            if list1 is None:
                tail.next = list2
                break
            elif list2 is None:
                tail.next = list1
                break
            
            if list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
            elif list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next

            tail = tail.next

        return dummy.next
