# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def rec(i, j):
            if i == j:
                return [None]
            res = []
            for k in range(i, j):
                left_trees = rec(i, k)
                right_trees = rec(k+1, j)
                for lt in left_trees:
                    for rt in right_trees:
                        res.append(TreeNode(k, lt, rt))
            return res
        
        return rec(1, n+1)
