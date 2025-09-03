# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def rec(tree, height):
            if not tree:
                return
            if len(ans) <= height:
                ans.append([])
            ans[height].append(tree.val)
            rec(tree.left, height+1)
            rec(tree.right, height+1)
        rec(root, 0)
        return ans