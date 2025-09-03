# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l_head = ListNode()
        r_head = ListNode()
        cur = head
        l_cur = l_head
        r_cur = r_head
        while cur != None:
            if cur.val < x:
                l_cur.next = cur
                l_cur = l_cur.next
            else:
                r_cur.next = cur
                r_cur = r_cur.next
            cur = cur.next
        l_cur.next = r_head.next
        r_cur.next = None
        return l_head.next
