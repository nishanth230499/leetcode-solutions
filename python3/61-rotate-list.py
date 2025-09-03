# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or k == 0:
            return head
        i = head
        length = 1
        while i.next != None:
            i = i.next
            length += 1
        k %= length
        i = head
        for _ in range(k):
            i = head if i.next == None else i.next
        j = head
        while i.next != None:
            i = i.next
            j = j.next
        
        i.next = head
        i = j.next
        j.next = None
        return i
