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
        new_head = ListNode(next=head)
        current = new_head
        while current and current.next and current.next.next:
            temp = current.next
            current.next = temp.next
            temp.next = current.next.next
            current.next.next = temp
            current = temp
        return new_head.next

        