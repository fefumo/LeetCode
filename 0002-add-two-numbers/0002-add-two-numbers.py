# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first = ""
        second = ""
        while l1:
            first += str(l1.val)
            l1 = l1.next
        while l2:
            second += str(l2.val)
            l2 = l2.next

        # print("before: ", first, ", ", second)
        first = first[::-1]
        second = second[::-1]
        total = int(first) + int(second)
        # print("after: ", first, ", ", second)
        
        dummy = ListNode()
        cur = dummy
        for digit in str(total)[::-1]:
            cur.next = ListNode(int(digit))
            cur = cur.next

        return dummy.next