# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        if head.next == None:
            return head
        dummy = ListNode(0)
        cur = head
        before_head = dummy
        while cur and cur.next: 
            first = cur
            second = cur.next
            
            before_head.next = second
            first.next = second.next
            second.next = first
            
            before_head = first
            cur = first.next
        return dummy.next
 