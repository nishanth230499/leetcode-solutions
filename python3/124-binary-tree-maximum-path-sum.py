# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec1(self, tree):
        if tree == None:
            return None, None
        l1, l2 = self.rec1(tree.left)
        r1, r2 = self.rec1(tree.right)
        sol1 = tree.val
        sol2 = tree.val
        if l1 != None:
            sol1 = max(sol1, l1, tree.val+l2)
            sol2 = max(sol2, tree.val + l2)
        if r1 != None:
            sol1 = max(sol1, r1, tree.val+r2)
            sol2 = max(sol2, tree.val + r2)
        if l1 != None and r1 != None:
            sol1 = max(sol1, l2+r2+tree.val)
        return sol1, sol2

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.rec1(root)[0]