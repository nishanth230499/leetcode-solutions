# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self, tree):
        if tree == None:
            return None
        sol = self.rec(tree.left)
        if sol != None:
            return sol
        self.c += 1
        if self.c == self.k:
            return tree.val
        sol = self.rec(tree.right)
        return sol
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.c = 0
        self.k = k
        return self.rec(root)
        