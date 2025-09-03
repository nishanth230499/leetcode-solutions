# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def rec(r, h):
            if r.left == None and r.right == None:
                return h
            res = float("INF")
            if r.left != None:
                res = min(res, rec(r.left, h+1))
            if r.right != None:
                res = min(res, rec(r.right, h+1))
            return res
        if root == None:
            return 0
        return rec(root, 1)
