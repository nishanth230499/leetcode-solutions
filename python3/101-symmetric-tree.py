# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def rec(r1, r2):
            if r1 == r2 == None:
                return True
            if r1 == None or r2 == None:
                return False
            if r1.val != r2.val:
                return False
            if not rec(r1.left, r2.right):
                return False
            if not rec(r1.right, r2.left):
                return False
            return True
        return rec(root, root)