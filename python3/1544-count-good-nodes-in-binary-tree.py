# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def rec(tree, high):
            if not tree:
                return 0
            ans = 0
            if tree.val >= high:
                ans += 1
            ans += rec(tree.left, max(high, tree.val))
            ans += rec(tree.right, max(high, tree.val))
            return ans
        return rec(root, float('-INF'))