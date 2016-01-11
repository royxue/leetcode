# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode('')
        dummy.next = head
        l1 = dummy
        while l1.next:
            l2 = l1.next
            if l2.val == l1.val:
                l1.next = l2.next
            else:
                l1 = l2
        return dummy.next