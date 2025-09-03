# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def rec(tree):
            flag, tree_min, tree_max = True, tree.val, tree.val
            if tree.left:
                l_flag, l_min, l_max = rec(tree.left)
                flag = flag and l_flag and tree.val > l_max
                tree_min = min(tree_min, l_min)
                tree_max = max(tree_max, l_max)
            if tree.right:
                r_flag, r_min, r_max = rec(tree.right)
                flag = flag and r_flag and tree.val < r_min
                tree_min = min(tree_min, r_min)
                tree_max = max(tree_max, r_max)
            return flag, tree_min, tree_max
        return rec(root)[0] if root else True
            