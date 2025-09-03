# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        frontier = [root]
        next_frontier = []
        order = 1
        res = []
        while len(frontier):
            tres = []
            if order == 1:
                for i in range(len(frontier)):
                    if frontier[i] != None:
                        tres.append(frontier[i].val)
                        next_frontier.append(frontier[i].left)
                        next_frontier.append(frontier[i].right)
                order = 0

            else:
                for i in range(len(frontier) - 1, -1, -1):
                    if frontier[i] != None:
                        tres.append(frontier[i].val)
                        next_frontier.append(frontier[i].right)
                        next_frontier.append(frontier[i].left)
                order = 1
                next_frontier.reverse()
            frontier = next_frontier
            next_frontier = []
            if len(tres):
                res.append(tres)
        return res