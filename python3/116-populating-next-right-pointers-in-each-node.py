"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]', ref = None) -> 'Optional[Node]':
        if root == None:
            return root
        root.next = ref
        self.connect(root.left, root.right)
        self.connect(root.right, None if ref == None else ref.left)
        return root
        