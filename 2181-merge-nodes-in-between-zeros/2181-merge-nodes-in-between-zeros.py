# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        cur_sum = 0
        head = head.next 
        cur_node = dummy
        while head is not None:
            if head.val != 0:
                cur_sum += head.val
            else:
                cur_node.next = ListNode(cur_sum)
                cur_node = cur_node.next
                cur_sum = 0
            head = head.next
        return dummy.next