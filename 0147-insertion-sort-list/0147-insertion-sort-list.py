# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fake_head = ListNode(0, head)
        cur = head.next
        prev = head
        
        while cur is not None:

            if cur.val >= prev.val:
                prev = cur
                cur = cur.next
            
            else:
                prev.next = cur.next
                insert = fake_head #for iterating from the beginning
                while cur.val > insert.next.val:
                    insert = insert.next
                #insert now shows the spot to place the node in
                cur.next = insert.next
                insert.next = cur
                cur = prev.next

        return fake_head.next
                