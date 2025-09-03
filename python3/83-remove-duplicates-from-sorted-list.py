# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur != None:
            next_node = cur
            while next_node != None and next_node.val == cur.val:
                next_node = next_node.next
            cur.next = next_node
            cur = cur.next
        return head