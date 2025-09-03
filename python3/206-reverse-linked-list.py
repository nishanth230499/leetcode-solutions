# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        current = head
        rev_head = None
        while current != None:
            next = current.next
            current.next = rev_head
            rev_head = current
            current = next
        return rev_head