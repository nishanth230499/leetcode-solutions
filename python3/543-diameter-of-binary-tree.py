# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode], init = True) -> int:
        if root == None:
            return 0 if init else (0,0)
        sol1 = self.diameterOfBinaryTree(root.left, False)
        sol2 = self.diameterOfBinaryTree(root.right, False)
        print(sol1, sol2)
        sol = sol1[1] + sol2[1]
        sol = max(sol, max(sol1[0], sol2[0]))
        if init:
            return sol
        else:
            h = max(sol1[1], sol2[1]) + 1
            return sol, h