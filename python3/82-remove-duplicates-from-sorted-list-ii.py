# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(None, head)
        cur = new_head
        while cur != None:
            if cur.next != None and cur.next.next != None and cur.next.val == cur.next.next.val:
                next_node = cur.next.next.next
                while next_node and next_node.val == cur.next.val:
                    next_node = next_node.next
                cur.next = next_node
            else:
                cur = cur.next
        return new_head.next

