# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        r = head
        for i in range(n):
            r = r.next
        
        if r == None:
            return head.next

        l = head
        while r.next != None:
            l = l.next
            r = r.next
        l.next = l.next.next
        return head
