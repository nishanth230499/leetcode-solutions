# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        frontier = [root]
        next_frontier = []
        res = []
        while len(frontier):
            t_res = []
            for ele in frontier:
                if ele != None:
                    t_res.append(ele.val)
                    next_frontier.append(ele.left)
                    next_frontier.append(ele.right)
            frontier = next_frontier
            next_frontier = []
            if len(t_res):
                res.append(t_res)
        res.reverse()
        return res
