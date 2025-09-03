# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def get_mid(h):
            fast = h
            slow = h
            if fast != None and fast.next != None:
                fast = fast.next.next
            else:
                return h
            while fast != None and fast.next != None:
                fast = fast.next.next
                slow = slow.next
            return slow
        if head ==None:
            return None
        mid = get_mid(head)
        if mid.next == None:
            return TreeNode(mid.val)
        root = mid.next
        mid.next = None
        return TreeNode(root.val, self.sortedListToBST(head), self.sortedListToBST(root.next))