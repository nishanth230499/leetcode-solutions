# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def rec(r):
            if r == None:
                return
            rec(r.left)
            rec(r.right)
            res.append(r.val)
        
        rec(root)
        return res