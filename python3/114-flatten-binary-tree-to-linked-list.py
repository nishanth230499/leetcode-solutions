# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode], extra = None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def rec(r, extra = None):
            if r == None:
                return extra
            r.right = rec(r.right, extra)
            r.right = rec(r.left, r.right)
            r.left = None
            return r
        
        rec(root)