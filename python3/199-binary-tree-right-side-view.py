# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def rec(tree, h):
            if not tree:
                return
            if len(ans) <= h:
                ans.append(tree.val)
            rec(tree.right, h+1)
            rec(tree.left, h+1)
        rec(root, 0)
        return ans