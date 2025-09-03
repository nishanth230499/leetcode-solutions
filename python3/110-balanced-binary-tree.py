# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode], init = True) -> bool:
        if root == None:
            return True if init else (True, 0)
        sol1 = self.isBalanced(root.left, False)
        sol2 = self.isBalanced(root.right, False)
        sol = sol1[0] and sol2[0] and abs(sol1[1] - sol2[1]) <= 1
        if init:
            return sol
        else:
            h = max(sol1[1], sol2[1]) + 1
            return sol, h
        