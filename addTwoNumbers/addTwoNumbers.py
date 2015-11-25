# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = ListNode(0)
        q = l
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            q.next = ListNode((x+y+carry)%10)
            carry = (x+y+carry)/10
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            q = q.next
        if carry > 0:
            q.next = ListNode(carry)
        return l.next
