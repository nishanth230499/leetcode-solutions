# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        head = ListNode(None, head)
        cur = head
        for _ in range(left - 1):
            cur = cur.next
        new_tail = cur.next
        new_cur = new_tail
        cur.next = new_cur.next
        for _ in range(right - left):
            temp = cur.next
            cur.next = temp.next
            temp.next = new_cur
            new_cur = temp
        new_tail.next = cur.next
        cur.next = new_cur
        return head.next

            

