# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        sec = slow.next
        slow.next = None

        new_sec = None
        while sec:
            next = sec.next
            sec.next = new_sec
            new_sec = sec
            sec = next
        sec = new_sec

        current = head
        while current and sec:
            next = current.next
            current.next = sec
            current = sec
            sec = sec.next
            current.next = next
            current = next